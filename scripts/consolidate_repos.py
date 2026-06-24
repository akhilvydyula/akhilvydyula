"""Delete all repos except the curated keep list (~10 flagship repos)."""
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

OWNER = "akhilvydyula"
ROOT = Path(__file__).resolve().parents[1]
KEEP_FILE = ROOT / "keep-repos.json"
MANIFEST = ROOT / "deleted-repos-manifest.json"


def list_all_repos() -> list[dict]:
    result = subprocess.run(
        [
            "gh",
            "repo",
            "list",
            OWNER,
            "--limit",
            "500",
            "--json",
            "name,isArchived,isFork,url,description,pushedAt",
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    return json.loads(result.stdout)


def delete_repo(name: str, dry_run: bool) -> bool:
    if dry_run:
        print(f"[dry-run] delete {OWNER}/{name}")
        return True

    result = subprocess.run(
        ["gh", "repo", "delete", f"{OWNER}/{name}", "--yes"],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        err = result.stderr.strip()
        if "delete_repo" in err:
            print("ERROR: gh needs delete_repo scope. Run:")
            print("  gh auth refresh -h github.com -s delete_repo")
            raise SystemExit(1)
        print(f"FAILED {name}: {err}")
        return False
    print(f"DELETED {name}")
    return True


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Consolidate to ~10 repos by deleting the rest")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--delay", type=float, default=0.5, help="Seconds between deletes")
    args = parser.parse_args()

    keep_data = json.loads(KEEP_FILE.read_text(encoding="utf-8"))
    keep = {entry["name"] for entry in keep_data["keep"]}

    all_repos = list_all_repos()
    to_delete = [r for r in all_repos if r["name"] not in keep]

    print(f"Total repos: {len(all_repos)}")
    print(f"Keeping: {len(keep)}")
    print(f"To delete: {len(to_delete)}")
    if args.dry_run:
        print("\n--- KEEP ---")
        for name in sorted(keep):
            print(f"  {name}")
        print("\n--- DELETE (first 20) ---")
        for r in to_delete[:20]:
            print(f"  {r['name']}")
        if len(to_delete) > 20:
            print(f"  ... and {len(to_delete) - 20} more")
        return

    deleted = []
    failed = []
    for repo in to_delete:
        name = repo["name"]
        if delete_repo(name, dry_run=False):
            deleted.append(repo)
        else:
            failed.append(repo)
        time.sleep(args.delay)

    manifest = {
        "deleted_at": datetime.now(timezone.utc).isoformat(),
        "owner": OWNER,
        "kept": sorted(keep),
        "deleted_count": len(deleted),
        "failed_count": len(failed),
        "deleted": deleted,
        "failed": [r["name"] for r in failed],
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"\nDone. Deleted {len(deleted)}, failed {len(failed)}")
    print(f"Manifest: {MANIFEST}")


if __name__ == "__main__":
    main()
