import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # 1. name and host_name have missing values
    df['name'] = df['name'].fillna('unknown')
    df['host_name'] = df['name'].fillna('unknown')

    # 2. last_review was str
    df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')

    # 3. min = 0, max = 10000 (reduce)
    # mean = 152.7 and meadian = 106 => right-skewed
    # IQR = 106, lowerbound = -90 = 0, upperbound = 334
    # 1000 is a loose bound, considering >334 already unusual, 
    # so we keep the boundary cases and cut only the extreme tail
    df = df[(df['price'] > 0) & (df['price'] <= 1000)]

    # 4. last_reviews flag
    df['has_reviews'] = df['last_review'].notna()

    # 5. duplicates 
    df = df.drop_duplicates(subset=['id'])

    return df
