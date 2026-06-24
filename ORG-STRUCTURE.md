# GitHub Organization Plan

Recommended structure to move from a flat **205-repo** personal account into clean, browsable groups.

## Current state (done)

- ✅ Every repo tagged with an `akhil-*` topic for GitHub filtering
- ✅ [REPOS.md](./REPOS.md) — full categorized catalog
- ✅ Automation scripts in [`scripts/`](./scripts/)

## Target structure

| Organization | Purpose | Repos to move | Example |
|--------------|---------|---------------|---------|
| **akhilvydyula** *(personal)* | Profile + pinned flagship work | Keep ~6 | `akhilvydyula`, `goalos-ai` |
| **akhilvydyula-labs** | Active engineering projects | 5–10 | `deploy_flask_app`, `Apply_Jobs_Dashboard` |
| **akhilvydyula-ml** | ML & data science portfolio | 30 | `Restaurant-Rating-Predict`, `Quora-Insincere-Questions-Classification` |
| **akhilvydyula-learn** | Courses, assignments, hackathons | 8 | `github-slideshow`, `Sentiment-Analysis-Hackathon` |
| **akhilvydyula-forks** | All forks (reference only) | 158 | `100-days-of-machine-learning`, awesome lists |
| **Akhilvydyula21** *(existing)* | Legacy ML coursework | 2+ | `applied-ml`, `machine-learning-online-2018` |

## Why organizations instead of folders?

GitHub does not support literal folders on personal accounts. **Organizations** are the native way to group repos under names like:

- `github.com/akhilvydyula-ml/Restaurant-Rating-Predict`
- `github.com/akhilvydyula-forks/awesome-datascience`

## Step 1 — Create organizations

Create these (free) at [github.com/organizations/plan](https://github.com/organizations/plan):

1. `akhilvydyula-labs`
2. `akhilvydyula-ml`
3. `akhilvydyula-learn`
4. `akhilvydyula-forks`

## Step 2 — Transfer repos (optional script)

After orgs exist, dry-run transfers:

```bash
python scripts/transfer_to_orgs.py --dry-run
python scripts/transfer_to_orgs.py --category forks
python scripts/transfer_to_orgs.py --category ml-projects
```

Transfers keep git history and fork relationships. You must be org owner + repo admin.

## Step 3 — Pin only your best work

On [github.com/akhilvydyula](https://github.com/akhilvydyula), pin up to 6 repos:

1. `goalos-ai` — flagship open source
2. `Restaurant-Rating-Predict` — NLP project
3. `deploy_flask_app` — engineering
4. `Akhil-Vydyula-PortfolioWebsite` — portfolio
5. `Quora-Insincere-Questions-Classification` — Kaggle ML
6. `data-driven-decision-making` — public resources

## Category → topic mapping

| Category | GitHub topic | Count |
|----------|--------------|------:|
| Profile | `akhil-profile` | 1 |
| Open Source | `akhil-opensource` | 2 |
| Web Apps | `akhil-web-apps` | 5 |
| ML & Data Science | `akhil-ml-projects` | 30 |
| Learning | `akhil-learning` | 8 |
| Portfolio | `akhil-portfolio` | 1 |
| Forks | `akhil-forks` | 158 |

## Maintenance

Re-run after adding new repos:

```bash
python scripts/categorize_repos.py
python scripts/apply_repo_topics.py
python scripts/generate_repos_md.py
```
