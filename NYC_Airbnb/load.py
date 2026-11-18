import pandas as pd
from sqlalchemy import create_engine, text

def load(df: pd.DataFrame, db_path: str = "data/clean/NYC_airbnb.db", table: str = "listings") -> None:
    engine = create_engine(f"sqlite:///{db_path}")

    with engine.begin() as conn:
        # Idempotence
        conn.execute(text(f"DROP TABLE IF EXISTS {table}"))

    df.to_sql(table, engine, if_exists="replace", index=False)

    with engine.connect() as conn:
        count = conn.execute(text(f"SELECT COUNT (*) FROM {table}")).scalar()
    # print(f"Uploaded: {count}")
