# Repository Structure (No Organizations)

Your repos stay on [@akhilvydyula](https://github.com/akhilvydyula) — organized like **folders** using name prefixes, topics, and archiving.

## Folder-like prefixes

GitHub has no real folders. Renaming repos with prefixes groups them when sorted by name:

| Prefix | Folder | Example |
|--------|--------|---------|
| `oss-` | Open Source | [oss-goalos-ai](https://github.com/akhilvydyula/oss-goalos-ai) |
| `ml-` | ML & Data Science | [ml-Restaurant-Rating-Predict](https://github.com/akhilvydyula/ml-Restaurant-Rating-Predict) |
| `web-` | Web Apps | [web-deploy_flask_app](https://github.com/akhilvydyula/web-deploy_flask_app) |
| `learn-` | Learning | [learn-task1](https://github.com/akhilvydyula/learn-task1) |
| `portfolio-` | Portfolio | [portfolio-Akhil-Vydyula-PortfolioWebsite](https://github.com/akhilvydyula/portfolio-Akhil-Vydyula-PortfolioWebsite) |
| `fork-` | Forks (archived) | [fork-awesome-datascience](https://github.com/akhilvydyula/fork-awesome-datascience) |

On your [Repositories](https://github.com/akhilvydyula?tab=repositories) tab, sort by **Name** to see them grouped.

## Other layers

| Layer | Purpose |
|-------|---------|
| **Topics** | `akhil-*` tags for GitHub search filters |
| **Archived forks** | 158 `fork-*` repos hidden from default view |
| **[REPOS.md](./REPOS.md)** | Full catalog with links |

## Quick filters

| Folder | Link |
|--------|------|
| Active projects (no forks) | [?q=-topic%3Aakhil-forks](https://github.com/akhilvydyula?tab=repositories&q=-topic%3Aakhil-forks) |
| ML | [?q=topic%3Aakhil-ml-projects](https://github.com/akhilvydyula?tab=repositories&q=topic%3Aakhil-ml-projects) |
| Open Source | [?q=topic%3Aakhil-opensource](https://github.com/akhilvydyula?tab=repositories&q=topic%3Aakhil-opensource) |
| Forks | [?q=topic%3Aakhil-forks](https://github.com/akhilvydyula?tab=repositories&q=topic%3Aakhil-forks) |

## Pin these 6 repos

1. [oss-goalos-ai](https://github.com/akhilvydyula/oss-goalos-ai)
2. [ml-Restaurant-Rating-Predict](https://github.com/akhilvydyula/ml-Restaurant-Rating-Predict)
3. [web-deploy_flask_app](https://github.com/akhilvydyula/web-deploy_flask_app)
4. [portfolio-Akhil-Vydyula-PortfolioWebsite](https://github.com/akhilvydyula/portfolio-Akhil-Vydyula-PortfolioWebsite)
5. [ml-Quora-Insincere-Questions-Classification](https://github.com/akhilvydyula/ml-Quora-Insincere-Questions-Classification)
6. [oss-data-driven-decision-making](https://github.com/akhilvydyula/oss-data-driven-decision-making)

## Scripts

```bash
python scripts/categorize_repos.py
python scripts/generate_repos_md.py
python scripts/apply_repo_topics.py
python scripts/prefix_rename.py --dry-run --category ml-projects
python scripts/archive_category.py --category forks
```
