--models/staging/stg_order_items.sql

SELECT
order_item_id, 
order_id, 
product_id, 
quantity, 
unit_price, 
discount

FROM {{source('raw','order_items')}}