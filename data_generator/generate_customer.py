from faker import Faker
import random
import pandas as pd

fake = Faker("en_AU")

customers = []

for customer_id in range(1, 10_001):

    customer = {
        "customer_id": customer_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "city": fake.city(),
        "state": fake.state_abbr(),
        "country": "Australia",
        "created_at": fake.date_between(
            start_date="-3y",
            end_date="today"
        ),
        "customer_status": random.choice([
            "active",
            "active",
            "active",
            "inactive"
        ])
    }

    customers.append(customer)

df = pd.DataFrame(customers)

df.to_csv(
    "data/customers.csv",
    index=False
)