from faker import Faker
import random
import pandas as pd

fake = Faker("en_AU")

customers_df = pd.read_csv("data/customers.csv")
customer_ids = customers_df["customer_id"].tolist()



orders = []

for order_id in range(1, 50001):
    order_status = random.choices(
    ["completed", "shipped", "processing", "cancelled"],
    weights=[50, 25, 15, 10]
    )[0]
    shipping_cost  = round(random.uniform(5, 30), 2)
    
    order = {
        "order_id": order_id,
        "customer_id" : random.choice(customer_ids),
        "order_date" : fake.date_between(
            start_date="-3y",
            end_date="today"
        ),
        "order_status" :  order_status,
        "shipping_city": fake.city(),
        "shipping_state" : fake.state(),
        "shipping_cost": shipping_cost 
    }
    orders.append(order)

df = pd.DataFrame(orders)

df.to_csv(
    "data/orders.csv",
    index=False
)