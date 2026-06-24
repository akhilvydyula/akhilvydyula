# Repository Structure (No Organizations)

Your **205 repos** stay on [@akhilvydyula](https://github.com/akhilvydyula) — organized with topics, archiving, and a profile catalog. No extra GitHub organizations required.

## How it works

| Layer | What it does |
|-------|----------------|
| **Topics** | Every repo has an `akhil-*` tag — filter on GitHub instantly |
| **Archive forks** | 158 forks archived → your default repo tab shows **~47 original projects** |
| **[REPOS.md](./REPOS.md)** | Full categorized index with links |
| **Profile README** | Quick-filter table for recruiters and visitors |
| **Pinned repos** | Up to 6 flagship projects on your profile |

## Browse by category

| Category | Filter on GitHub |
|----------|------------------|
| Open Source | [topic:akhil-opensource](https://github.com/akhilvydyula?tab=repositories&q=topic%3Aakhil-opensource) |
| ML & Data Science | [topic:akhil-ml-projects](https://github.com/akhilvydyula?tab=repositories&q=topic%3Aakhil-ml-projects) |
| Web Apps | [topic:akhil-web-apps](https://github.com/akhilvydyula?tab=repositories&q=topic%3Aakhil-web-apps) |
| Learning | [topic:akhil-learning](https://github.com/akhilvydyula?tab=repositories&q=topic%3Aakhil-learning) |
| Forks (archived) | [topic:akhil-forks](https://github.com/akhilvydyula?tab=repositories&q=topic%3Aakhil-forks+archived%3Atrue) |
| Active only (no forks) | [exclude forks](https://github.com/akhilvydyula?tab=repositories&q=-topic%3Aakhil-forks) |

## Pin these 6 repos on your profile

On [github.com/akhilvydyula](https://github.com/akhilvydyula) → **Customize your pins**:

1. [goalos-ai](https://github.com/akhilvydyula/goalos-ai)
2. [Restaurant-Rating-Predict](https://github.com/akhilvydyula/Restaurant-Rating-Predict)
3. [deploy_flask_app](https://github.com/akhilvydyula/deploy_flask_app)
4. [Akhil-Vydyula-PortfolioWebsite](https://github.com/akhilvydyula/Akhil-Vydyula-PortfolioWebsite)
5. [Quora-Insincere-Questions-Classification](https://github.com/akhilvydyula/Quora-Insincere-Questions-Classification)
6. [data-driven-decision-making](https://github.com/akhilvydyula/data-driven-decision-making)

## Scripts

```bash
# Rebuild inventory + catalog
python scripts/categorize_repos.py
python scripts/generate_repos_md.py
python scripts/apply_repo_topics.py

# Archive all forks (clean default repo list)
python scripts/archive_category.py --category forks

# Restore forks if needed
python scripts/archive_category.py --category forks --unarchive
```

## Category counts

| Category | Topic | Count |
|----------|-------|------:|
| Profile | `akhil-profile` | 1 |
| Open Source | `akhil-opensource` | 2 |
| Web Apps | `akhil-web-apps` | 5 |
| ML & Data Science | `akhil-ml-projects` | 30 |
| Learning | `akhil-learning` | 8 |
| Portfolio | `akhil-portfolio` | 1 |
| Forks | `akhil-forks` | 158 |
