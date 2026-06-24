"""Transfer categorized repos to GitHub organizations."""
import json
import subprocess
import time
from pathlib import Path

INVENTORY = Path(__file__).resolve().parents[1] / "repo-inventory.json"
OWNER = "akhilvydyula"

ORG_MAP = {
    "forks": "akhilvydyula-forks",
    "ml-projects": "akhilvydyula-ml",
    "learning": "akhilvydyula-learn",
    "opensource": "akhilvydyula-labs",
    "development": "akhilvydyula-labs",
    "web-apps": "akhilvydyula-labs",
    "portfolio": "akhilvydyula-labs",
}


def transfer(repo: str, org: str, dry_run: bool = False) -> bool:
    if dry_run:
        print(f"[dry-run] {OWNER}/{repo} -> {org}/{repo}")
        return True

    result = subprocess.run(
        [
            "gh",
            "api",
            f"repos/{OWNER}/{repo}/transfer",
            "-X",
            "POST",
            "-f",
            f"new_owner={org}",
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        print(f"FAILED {repo}: {result.stderr.strip()}")
        return False
    print(f"OK {repo} -> {org}")
    return True


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--category", required=True, choices=list(ORG_MAP))
    args = parser.parse_args()

    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    repos = inventory["categories"].get(args.category, [])
    org = ORG_MAP[args.category]

    ok = 0
    for repo in repos:
        if transfer(repo["name"], org, dry_run=args.dry_run):
            ok += 1
        time.sleep(1)

    print(f"Transferred {ok}/{len(repos)} to {org}")


if __name__ == "__main__":
    main()
