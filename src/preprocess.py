import pandas as pd

FUNNEL_MAP = {"view": "View", "cart": "Add to Cart", "purchase": "Purchase"}
TIME_COL_CANDIDATES = ["event_time", "event_time_utc", "event_datetime", "timestamp", "time"]

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def get_time_col(df: pd.DataFrame) -> str:
    for c in TIME_COL_CANDIDATES:
        if c in df.columns:
            return c
    raise KeyError(f"Time column not found. Available columns: {df.columns.tolist()}")

def prepare_funnel(df: pd.DataFrame) -> pd.DataFrame:
    time_col = get_time_col(df)
    df[time_col] = pd.to_datetime(df[time_col], errors="coerce", utc=True)
    df = df.dropna(subset=[time_col])

    df["funnel_stage"] = df["event_type"].map(FUNNEL_MAP)
    df = df[df["funnel_stage"].notna()]

    return df