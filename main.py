import pandas as pd

df = pd.read_csv("data/payments.csv")


print(df.head())
print(df.shape)
print(df["payment_status"].value_counts())
print(df["payment_method"].value_counts())
successful_payments = (
    df[df["payment_status"] == "successful"]
    .groupby("order_id")
    .size()
)

print(successful_payments.max())
print(df["payment_status"].value_counts())