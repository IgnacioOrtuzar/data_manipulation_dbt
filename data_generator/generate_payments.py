from faker import Faker
import random
import pandas as pd
from datetime import timedelta

fake = Faker("en_AU")

order_df = pd.read_csv(
    "data/orders.csv",
    parse_dates=["order_date"]
)
order_ids = order_df["order_id"].tolist()

# Create lookup: order_id -> order_date
order_date_lookup = dict(
    zip(
        order_df["order_id"],
        order_df["order_date"]
    )
)

order_items = pd.read_csv("data/order_items.csv")

# Calculate total for each order
order_items["line_total"] = (
    order_items["quantity"]
    * order_items["unit_price"]
    * (1 - order_items["discount"] / 100)
)

order_totals = (
    order_items
    .groupby("order_id")["line_total"]
    .sum()
    .to_dict()
)
payment_methods = ["credit_card", "debit_card", "paypal", "bank_transfer"]

payment_id = 1
payments = []

for order_id in order_ids:

    number_payments =random.choices(
    [1, 2, 3],
    weights=[90, 7, 3]
    )[0]
    order_date = order_date_lookup[order_id]
    amount = round(order_totals[order_id], 2)

    for attempt_number in range(1, number_payments + 1):

        if attempt_number < number_payments:
            status = "failed"
        else:
            status = random.choices(
                ["successful", "failed"],
                weights=[95, 5]
            )[0]

        payment_date = (
                        order_date
                        + timedelta(days=attempt_number - 1)
                    )
        payment = {
            "payment_id":payment_id,
            "order_id": order_id,
            "payment_date": payment_date,
            "payment_method": random.choice(payment_methods),
            "payment_status": status,
            "amount" :  amount

        }

        payments.append(payment)
        payment_id +=1


df = pd.DataFrame(payments)

df.to_csv(
    "data/payments.csv",
    index=False
)
