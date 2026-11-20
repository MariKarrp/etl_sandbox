# ETL Sandbox

A personal sandbox for practising **ETL (Extract → Transform → Load)** pipelines on real, messy datasets. Each subfolder is a self-contained mini-project: a source dataset, a cleaning/transformation logic, and a load step into a database.

The goal is not to build a production system, but to **practise the core patterns** that show up in real data engineering work: handling missing values, fixing types, dropping outliers, ensuring idempotency, logging, and documenting decisions.

## Projects

| Project | Dataset | Stack | What it practises |
|---|---|---|---|
| [`NYC_Airbnb`](./NYC_Airbnb) | NYC Airbnb listings (Kaggle) | Python, pandas, SQLAlchemy, SQLite | Cleaning a dirty CSV: missing values, datetime casting, outlier removal, duplicate checks, idempotent load |

More projects will be added over time (API sources, PostgreSQL, Airflow orchestration, dbt transformations).

## Repository structure

```
etl_sandbox/
├── NYC_Airbnb/ # first project
│ ├── data/
│ │ ├── raw/ # source CSV (not committed)
│ │ └── clean/ # output database (not committed)
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ ├── pipeline.py # orchestrator
│ └── README.md # project-specific details
└── README.md # this file
```

## How to run a project

Each project is self-contained. General pattern:

```bash
cd NYC_Airbnb
pip install pandas sqlalchemy
python pipeline.py
```
See the project's own README.md for dataset download instructions and design decisions.

## Conventions used across projects

- Code and comments in English.
- Data is not committed - only code and documentation. Each project's README explains where to get the source data.
- Idempotent loads - re-running a pipeline does not duplicate rows.
- Logging instead of print - pipeline stages are logged with timestamps.
- Design decisions are documented - why a cutoff was chosen, why missing values were flagged rather than imputed, etc.

## Why this repo exists

I'm learning data engineering by building. This sandbox is where I turn theory into working pipelines, one messy dataset at a time :/