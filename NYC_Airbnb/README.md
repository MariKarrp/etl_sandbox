# etl-sandbox/NYC_Airbnb

An ETL pipeline that cleans a "dirty" NYC Airbnb dataset and loads it into SQLite.

## What it does
1. **Extract** - reads a CSV (`data/raw/...`) with pandas.
2. **Transform** - cleans the data:
   - casts `last_review` to datetime;
   - fills missing `name` and `host_name` with `unknown`;
   - creates a `has_reviews` flag (missing review = a fact, not an error);
   - drops listings with `price <= 0` and `price > 1000` (outliers);
   - checks for duplicate `id`s.
3. **Load** - idempotently writes the result into the `listings` table in SQLite.

## Results
- Rows before: 48,895
- Rows after: 48,645
- Dropped by price: 250
- Duplicate ids: 0

## Data
Download the [NYC Airbnb dataset](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data) from Kaggle

Place the CSV file into `data/raw/`. The pipeline will create `data/clean/NYC_airbnb.db` automatically.

## How to run
```bash
pip install pandas sqlalchemy
python pipeline.py
```

## Design decisions

- The price <= 1000 cutoff is based on stats: the 75th percentile is 175, so anything above 1000 is a rare luxury listing that skews averages.

- Missing last_review is not imputed but flagged: it's a logical absence (no reviews yet), not a data error.

