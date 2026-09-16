SELECT 
order_id, 
customer_id, 
order_date, 
order_status, 
shipping_city, 
shipping_state, 
shipping_cost

FROM {{source('raw','orders')}}