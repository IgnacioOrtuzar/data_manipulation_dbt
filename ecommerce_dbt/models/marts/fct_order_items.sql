select
    ioie.order_item_id,
    ioie.order_id,
    o.customer_id,
    o.order_date,
    o.order_status,
    ioie.product_id,
    ioie.quantity,
    ioie.unit_price,
    ioie.discount,
    ioie.gross_amount,
    ioie.discount_amount,
    ioie.net_amount,
    ioie.total_cost,
    ioie.gross_margin
from
    {{ref ('int_order_items_enriched')}} as ioie

left join {{ref('stg_orders')}} as o
            ON ioie.order_id = o.order_id
