import pandas as pd

FUNNEL_ORDER = ["View", 
                "Add to Cart", 
                "Purchase"]

def calculate_funnel_behaviour(df: pd.DataFrame) -> pd.DataFrame:
    counts = (
        df.groupby("funnel_stage")["user_id"]
        .nunique()
        .reindex(FUNNEL_ORDER)
    )

    conversion_rate = counts / counts.shift(1)
    
    return pd.DataFrame({
            "users": counts,
            "conversion_rate": conversion_rate
    })


def calculate_funnel_strict(df: pd.DataFrame) -> pd.DataFrame:
    """
    Strict funnel:
    - Cart count = users who have View AND Add to Cart
    - Purchase count = users who have View AND Add to Cart AND Purchase
    Ensures monotonic decrease (View >= Cart >= Purchase)
    """
    
    user_stages = (
        df.groupby("user_id")["funnel_stage"]
          .apply(set)
    )

    view_users = user_stages[user_stages.apply(lambda s: "View" in s)].index
    cart_users = user_stages[user_stages.apply(lambda s: {"View", "Add to Cart"}.issubset(s))].index
    purchase_users = user_stages[user_stages.apply(lambda s: {"View", "Add to Cart", "Purchase"}.issubset(s))].index

    counts = pd.Series(
        [len(view_users), len(cart_users), len(purchase_users)],
        index=FUNNEL_ORDER,
        name="users"
    )

    conversion_rate = counts / counts.shift(1)

    return pd.DataFrame({
        "users": counts,
        "conversion_rate": conversion_rate
    })
