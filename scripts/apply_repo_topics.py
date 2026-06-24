"""Apply GitHub topics to categorize repositories."""
import json
import subprocess
import time
from pathlib import Path

OWNER = "akhilvydyula"
INVENTORY = Path(__file__).resolve().parents[1] / "repo-inventory.json"

CATEGORY_TOPICS = {
    "profile": ["akhil-profile", "github-profile"],
    "portfolio": ["akhil-portfolio", "web"],
    "opensource": ["akhil-opensource", "open-source"],
    "development": ["akhil-development", "software-engineering"],
    "web-apps": ["akhil-web-apps", "web-development"],
    "ml-projects": ["akhil-ml-projects", "machine-learning", "data-science"],
    "learning": ["akhil-learning", "education", "coursework"],
    "forks": ["akhil-forks", "fork"],
    "misc": ["akhil-misc"],
}


def apply_topics(repo_name: str, topics: list[str], dry_run: bool = False) -> bool:
    payload = json.dumps({"names": topics})
    if dry_run:
        print(f"[dry-run] {repo_name}: {topics}")
        return True

    result = subprocess.run(
        [
            "gh",
            "api",
            f"repos/{OWNER}/{repo_name}/topics",
            "-X",
            "PUT",
            "-H",
            "Accept: application/vnd.github.mercy-preview+json",
            "--input",
            "-",
        ],
        input=payload,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        print(f"FAILED {repo_name}: {result.stderr.strip()}")
        return False
    return True


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--category", help="Only apply to one category")
    args = parser.parse_args()

    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    categories = inventory["categories"]

    total = 0
    failed = 0

    for category, repos in categories.items():
        if args.category and category != args.category:
            continue
        topics = CATEGORY_TOPICS.get(category, [f"akhil-{category}"])
        for repo in repos:
            total += 1
            ok = apply_topics(repo["name"], topics, dry_run=args.dry_run)
            if not ok:
                failed += 1
            time.sleep(0.35)

    print(f"Processed {total} repos, failed {failed}")


if __name__ == "__main__":
    main()
