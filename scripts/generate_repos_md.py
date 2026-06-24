"""Generate REPOS.md catalog from repo inventory."""
import json
from pathlib import Path

INVENTORY = Path(__file__).resolve().parents[1] / "repo-inventory.json"
OUTPUT = Path(__file__).resolve().parents[1] / "REPOS.md"

META = {
    "profile": ("Profile", "GitHub profile and identity repos"),
    "opensource": ("Open Source", "Active public projects and contributions"),
    "development": ("Development", "Engineering and application code"),
    "web-apps": ("Web Apps", "Websites, dashboards, and Flask apps"),
    "ml-projects": ("ML & Data Science", "Machine learning notebooks and Kaggle-style projects"),
    "learning": ("Learning & Coursework", "Courses, assignments, hackathons, and tutorials"),
    "portfolio": ("Portfolio", "Personal branding and portfolio sites"),
    "forks": ("Forks", "Forked repositories for reference and experimentation"),
    "misc": ("Miscellaneous", "Other repositories"),
}

ORDER = [
    "profile",
    "opensource",
    "development",
    "web-apps",
    "ml-projects",
    "learning",
    "portfolio",
    "misc",
    "forks",
]


def repo_line(repo: dict) -> str:
    desc = (repo.get("description") or "").strip().replace("\n", " ")
    if len(desc) > 100:
        desc = desc[:97] + "..."
    lang = repo.get("language") or "—"
    suffix = f" — {desc}" if desc else ""
    return f"- [{repo['name']}]({repo['url']}) `{lang}`{suffix}"


def main():
    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    categories = inventory["categories"]
    summary = inventory["summary"]

    lines = [
        "# Repository Catalog",
        "",
        "Organized index of all repositories under [@akhilvydyula](https://github.com/akhilvydyula).",
        "",
        f"**Total:** {inventory['total']} repositories",
        "",
        "## Quick filters (GitHub topics)",
        "",
        "| Topic | Category | Count |",
        "|-------|----------|------:|",
    ]

    for key in ORDER:
        if key not in summary:
            continue
        title, _ = META[key]
        lines.append(f"| `akhil-{key}` | {title} | {summary[key]} |")

    lines.extend(
        [
            "",
            "> Filter on GitHub: `https://github.com/akhilvydyula?tab=repositories&q=topic%3Aakhil-ml-projects`",
            "",
            "---",
            "",
        ]
    )

    for key in ORDER:
        repos = categories.get(key, [])
        if not repos:
            continue
        title, blurb = META[key]
        lines.append(f"## {title} ({len(repos)})")
        lines.append("")
        lines.append(blurb + ".")
        lines.append("")
        if key == "forks" and len(repos) > 15:
            lines.extend(repo_line(r) for r in repos[:15])
            lines.append("")
            lines.append(
                f"<details><summary><strong>View all {len(repos)} forks</strong></summary>"
            )
            lines.append("")
            lines.extend(repo_line(r) for r in repos[15:])
            lines.append("")
            lines.append("</details>")
        else:
            lines.extend(repo_line(r) for r in repos)
        lines.append("")

    OUTPUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
