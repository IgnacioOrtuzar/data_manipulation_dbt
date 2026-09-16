from faker import Faker
import random
import pandas as pd

fake = Faker("en_AU")

active = random.choices(
    [True, False],
    weights=[85, 15]
)[0]

products_by_category = {
    "Electronics": [
        "Wireless Mouse",
        "Mechanical Keyboard",
        "USB-C Charger",
        "Bluetooth Speaker",
        "Webcam"
    ],

    "Clothing": [
        "Cotton T-Shirt",
        "Hoodie",
        "Running Shorts",
        "Jacket",
        "Jeans"
    ],

    "Sports": [
        "Yoga Mat",
        "Dumbbells",
        "Resistance Bands",
        "Football",
        "Water Bottle"
    ],

    "Home": [
        "Desk Lamp",
        "Coffee Mug",
        "Pillow",
        "Storage Box",
        "Kitchen Knife"
    ]
}

products = []

for product_id in range(1, 10_001):
    category = random.choice(list(products_by_category.keys()))
    product_name = random.choice(products_by_category[category])
    price = round(random.uniform(10, 500), 2)
    cost_percentage = random.uniform(0.40, 0.75)
    cost = round(price * cost_percentage, 2)

    active = random.choices(
    [True, False],
    weights=[85, 15]
    )[0]

    product = {
        "product_id": product_id,
        "product_name": product_name,
        "category": category,
        "price" : price,
        "cost": cost,
        "created_at": fake.date_between(
            start_date="-3y",
            end_date="today"
        ),
        "product_status": active
    }

    products.append(product)

df = pd.DataFrame(products)

df.to_csv(
    "data/products.csv",
    index=False
)