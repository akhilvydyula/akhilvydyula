"""Categorize akhilvydyula GitHub repos for restructuring."""
import json
import subprocess
from collections import defaultdict
from pathlib import Path

OWNER = "akhilvydyula"

RULES = [
    ("profile", lambda r: r["name"] == "akhilvydyula"),
    ("forks", lambda r: r.get("fork")),
    ("portfolio", lambda r: "portfolio" in r["name"].lower()),
    (
        "opensource",
        lambda r: r["name"] in {"goalos-ai", "data-driven-decision-making"}
        or "open-source" in (r.get("description") or "").lower(),
    ),
    (
        "web-apps",
        lambda r: any(
            x in r["name"].lower()
            for x in ["webapp", "flask", "dashboard", "portfolio", "movie-recommendation"]
        )
        or r.get("language") == "HTML",
    ),
    (
        "learning",
        lambda r: any(
            x in r["name"].lower()
            for x in [
                "assignment",
                "course",
                "hackathon",
                "slideshow",
                "task1",
                "zeta",
                "uhack",
                "younity",
                "c-assignment",
                "devops",
                "solvers-challenge",
            ]
        ),
    ),
    (
        "ml-projects",
        lambda r: r.get("language") == "Jupyter Notebook"
        or any(
            x in r["name"].lower()
            for x in [
                "predict",
                "classification",
                "sentiment",
                "detection",
                "analysis",
                "dataset",
                "kaggle",
                "quora",
                "netflix",
                "malware",
                "cancer",
                "breast",
                "taxi",
                "movie",
                "restaurant",
                "stackoverflow",
                "twitter",
                "fake-news",
                "car-price",
                "donor",
                "facebook",
                "news",
                "apparel",
                "amazon",
                "heberman",
                "human_activity",
                "santander",
                "credit-risk",
                "fashion",
                "identify",
                "automate",
                "bing_search",
                "speech",
                "medical",
                "tea-story",
                "personalized",
            ]
        ),
    ),
    (
        "development",
        lambda r: r.get("language") in {"Python", "TypeScript", "JavaScript"}
        and not r.get("fork"),
    ),
]


def gh_api(path: str):
    result = subprocess.run(
        ["gh", "api", path],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    return json.loads(result.stdout)


def categorize(repo: dict) -> str:
    for category, rule in RULES:
        if rule(repo):
            return category
    return "misc"


def fetch_repos() -> list[dict]:
    repos = []
    for page in range(1, 4):
        batch = gh_api(f"users/{OWNER}/repos?per_page=100&page={page}&sort=updated")
        if not batch:
            break
        repos.extend(batch)
    return repos


def main():
    repos = fetch_repos()
    grouped: dict[str, list[dict]] = defaultdict(list)

    for repo in repos:
        category = categorize(repo)
        grouped[category].append(
            {
                "name": repo["name"],
                "fork": repo.get("fork", False),
                "private": repo.get("private", False),
                "language": repo.get("language"),
                "description": repo.get("description") or "",
                "url": repo["html_url"],
                "updated_at": repo.get("updated_at"),
                "category": category,
                "topic": f"akhil-{category}",
            }
        )

    output = {
        "owner": OWNER,
        "total": len(repos),
        "summary": {k: len(v) for k, v in sorted(grouped.items())},
        "categories": {k: sorted(v, key=lambda x: x["name"].lower()) for k, v in sorted(grouped.items())},
    }

    out_path = Path(__file__).resolve().parents[1] / "repo-inventory.json"
    out_path.write_text(json.dumps(output, indent=2), encoding="utf-8")

    print(f"Total repos: {len(repos)}")
    for category, items in sorted(output["summary"].items()):
        print(f"  {category}: {items}")
    print(f"Saved {out_path}")


if __name__ == "__main__":
    main()
