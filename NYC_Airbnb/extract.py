import pandas as pd

def extract(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    # print(f"# strings: {len(df)}, # columns: {len(df.columns)}")
    # print(f"\nColumns types: \n{df.dtypes}")
    # print(f"\nMissings: \n{df.isna().sum()}")
    # print(f"\nFirst 5 rows: \n{df.head()}")

    return df
