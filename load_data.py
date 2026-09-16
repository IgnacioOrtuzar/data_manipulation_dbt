import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/ecommerce"
)

tables = [
    "customers",
    "products",
    "orders",
    "order_items",
    "payments"
]

for table in tables:

    df = pd.read_csv(f"data/{table}.csv")

    df.to_sql(
        name=table,
        con=engine,
        schema="raw",
        if_exists="append",
        index=False
    )

    print(f"{table} loaded: {len(df)} rows")