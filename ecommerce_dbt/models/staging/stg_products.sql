SELECT 

product_id, 
product_name, 
category, 
price, 
cost, 
created_at, 
product_status

FROM {{source('raw','products')}}