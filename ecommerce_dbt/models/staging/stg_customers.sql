-- models/staging/stg_customers.sql

select
    customer_id,
    first_name,
    last_name,
    email,
    city,
    state,
    country,
    created_at,
    customer_status

from {{ source('raw', 'customers') }}