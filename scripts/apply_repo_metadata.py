"""Apply strong descriptions, homepages, and topics from repo-inventory.json."""
import json
import subprocess
import time
from pathlib import Path

OWNER = "akhilvydyula"
INVENTORY = Path(__file__).resolve().parents[1] / "repo-inventory.json"


def patch_repo(repo: dict, dry_run: bool) -> None:
    name = repo["name"]
    payload = {"description": repo["description"][:350]}
    if repo.get("demo"):
        payload["homepage"] = repo["demo"]

    if dry_run:
        print(f"[dry-run] PATCH {name}: {payload['description'][:80]}...")
        print(f"          topics: {repo['topics']}")
        return

    result = subprocess.run(
        ["gh", "api", f"repos/{OWNER}/{name}", "-X", "PATCH"]
        + [arg for k, v in payload.items() for arg in ("-f", f"{k}={v}")],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        print(f"FAILED patch {name}: {result.stderr.strip()}")
        return
    print(f"OK patch {name}")

    topics = json.dumps({"names": repo["topics"]})
    result = subprocess.run(
        [
            "gh",
            "api",
            f"repos/{OWNER}/{name}/topics",
            "-X",
            "PUT",
            "--input",
            "-",
        ],
        input=topics,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        print(f"FAILED topics {name}: {result.stderr.strip()}")
    else:
        print(f"OK topics {name}")


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    data = json.loads(INVENTORY.read_text(encoding="utf-8"))
    for repo in data["repos"]:
        patch_repo(repo, dry_run=args.dry_run)
        time.sleep(0.4)


if __name__ == "__main__":
    main()
