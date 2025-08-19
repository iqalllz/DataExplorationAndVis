import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Load dataset BMW dari CSV"""
    return pd.read_csv(path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning: drop duplicates, handle missing"""
    df = df.drop_duplicates()
    df = df.dropna(how="all")
    return df