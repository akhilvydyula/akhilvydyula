"""Archive or unarchive repos by category from repo-inventory.json."""
import json
import subprocess
import time
from pathlib import Path

OWNER = "akhilvydyula"
INVENTORY = Path(__file__).resolve().parents[1] / "repo-inventory.json"


def set_archived(repo: str, archived: bool, dry_run: bool = False) -> bool:
    action = "archive" if archived else "unarchive"
    if dry_run:
        print(f"[dry-run] {action} {OWNER}/{repo}")
        return True

    result = subprocess.run(
        [
            "gh",
            "api",
            f"repos/{OWNER}/{repo}",
            "-X",
            "PATCH",
            "-f",
            f"archived={'true' if archived else 'false'}",
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        print(f"FAILED {repo}: {result.stderr.strip()}")
        return False
    print(f"OK {action} {repo}")
    return True


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--category", required=True)
    parser.add_argument("--unarchive", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    repos = inventory["categories"].get(args.category, [])
    archived = not args.unarchive

    ok = 0
    for repo in repos:
        if repo["name"] == "akhilvydyula":
            continue
        if set_archived(repo["name"], archived, dry_run=args.dry_run):
            ok += 1
        time.sleep(0.4)

    print(f"Done: {ok}/{len(repos)} repos")


if __name__ == "__main__":
    main()
