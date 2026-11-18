import logging
from extract import extract
from transform import transform
from load import load

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",)

CSV_PATH = "data/raw/AB_NYC_2019.csv"
DB_PATH = "data/clean/NYC_airbnb.db"
TABLE = "listings"

def run():
    logging.info("Starting ETL-pipeline...")
    df_raw = extract(CSV_PATH)
    logging.info("Extract done: %d rows", len(df_raw))

    df = transform(df_raw)
    logging.info("Transform done: %d rows", len(df))

    load(df, db_path=DB_PATH, table=TABLE)
    logging.info("Load done. Pipeline completed")

if __name__ == "__main__":
    run()