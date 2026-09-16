WITH order_items_with_products as (
    SELECT
        oi.order_item_id,
        oi.order_id,
        oi.product_id,
        oi.quantity,
        oi.unit_price,
        oi.discount,
        p.product_name,
        p.category,
        p.cost
    from
        {{ref('stg_order_items')}} as oi
    left join {{ref('stg_products')}} as p
    on oi.product_id = p.product_id
),

gross_metrics as (

    select
        *,
        quantity * unit_price as gross_amount,
        quantity * cost as total_cost

    from order_items_with_products
),

discount_metrics as (

    select
        *,
        gross_amount * (discount / 100.0) as discount_amount

    from gross_metrics
),

net_metrics as (

    select
        *,
        gross_amount - discount_amount as net_amount

    from discount_metrics
)


select
    *,
    net_amount - total_cost as gross_margin

from net_metrics