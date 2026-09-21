select
    product_id, 
    product_name, 
    category, 
    price, 
    cost, 
    created_at, 
    product_status
from {{ ref('stg_products') }}