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
    
from {{ ref('stg_customers') }}