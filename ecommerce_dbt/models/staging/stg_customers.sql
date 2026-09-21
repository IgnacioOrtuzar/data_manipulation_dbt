-- models/staging/stg_customers.sql

select
        customer_id,
    initcap(trim(first_name)) as first_name,
    initcap(trim(last_name)) as last_name,
    lower(trim(email)) as email,
    initcap(trim(city)) as city,
    upper(trim(state)) as state,
    initcap(trim(country)) as country,
    created_at,
    lower(trim(customer_status)) as customer_status

from {{ source('raw', 'customers') }}