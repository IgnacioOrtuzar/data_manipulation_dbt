from faker import Faker
import random
import pandas as pd

fake = Faker("en_AU")

order_df = pd.read_csv("data/orders.csv")
order_ids = order_df["order_id"].tolist()

product_df = pd.read_csv("data/products.csv")
product_ids =  product_df['product_id'].to_list()
product_price_lookup = dict(
    zip(product_df["product_id"], product_df["price"])
)


order_item_list = []
order_item_id = 1

for order_id in order_ids:

    number_of_items = random.randint(1, 5)

    for _ in range(number_of_items):

        product_id = random.choice(product_ids)
        unit_price = product_price_lookup[product_id]

        order_item = {
            "order_item_id": order_item_id,
            "order_id" : order_id,
            "product_id": product_id,
            "quantity" : random.randint(1, 5),
            "unit_price": unit_price,
            "discount" : random.choice([0,5,10,20])
        }

        order_item_list.append(order_item)
        order_item_id += 1

df = pd.DataFrame(order_item_list)

df.to_csv(
    "data/order_items.csv",
    index=False
)