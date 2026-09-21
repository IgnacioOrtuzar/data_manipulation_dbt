select
    product_id,
    initcap(trim(product_name)) as product_name,
    lower(trim(category)) as category,
    cast(price as numeric(10,2)) as price,
    cast(cost as numeric(10,2)) as cost,
    created_at,
    product_status

from {{ ref('stg_products') }}