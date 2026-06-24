"""Rename repos with category prefixes for folder-like grouping on GitHub."""
import json
import subprocess
import time
from pathlib import Path

OWNER = "akhilvydyula"
INVENTORY = Path(__file__).resolve().parents[1] / "repo-inventory.json"

PREFIX = {
    "profile": None,
    "forks": "fork",
    "ml-projects": "ml",
    "learning": "learn",
    "web-apps": "web",
    "opensource": "oss",
    "portfolio": "portfolio",
    "development": "dev",
    "misc": "misc",
}


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
        print(f"FAILED {action} {repo}: {result.stderr.strip()}")
        return False
    return True


def rename_repo(old: str, new: str, dry_run: bool = False) -> bool:
    if old == new:
        return True
    if dry_run:
        print(f"[dry-run] {old} -> {new}")
        return True

    result = subprocess.run(
        ["gh", "api", f"repos/{OWNER}/{old}", "-X", "PATCH", "-f", f"name={new}"],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        print(f"FAILED {old} -> {new}: {result.stderr.strip()}")
        return False
    print(f"OK {old} -> {new}")
    return True


def target_name(category: str, name: str) -> str | None:
    prefix = PREFIX.get(category)
    if not prefix:
        return None
    if name.startswith(f"{prefix}-"):
        return name
    return f"{prefix}-{name}"


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--category", help="Only rename one category")
    args = parser.parse_args()

    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    ok = failed = skipped = 0

    for category, repos in inventory["categories"].items():
        if args.category and category != args.category:
            continue
        for repo in repos:
            old = repo["name"]
            new = target_name(category, old)
            if not new:
                skipped += 1
                continue

            if category == "forks" and not args.dry_run:
                if not set_archived(old, False):
                    failed += 1
                    continue
                time.sleep(0.3)

            if rename_repo(old, new, dry_run=args.dry_run):
                ok += 1
                if category == "forks" and not args.dry_run:
                    time.sleep(0.3)
                    set_archived(new, True)
            else:
                failed += 1
                if category == "forks" and not args.dry_run:
                    set_archived(old, True)
            time.sleep(0.5)

    print(f"Renamed {ok}, failed {failed}, skipped {skipped}")


if __name__ == "__main__":
    main()
