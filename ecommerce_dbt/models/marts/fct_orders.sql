with order_item_totals as (
    SELECT
        order_id, 
        sum(gross_amount) as total_gross_amount,
        sum(total_cost) as complete_total_cost,
        sum(discount_amount) as total_discount_amount,
        sum(net_amount) as total_net_amount,
        sum(gross_margin) as total_gross_margin

        from
            {{ref ('int_order_items_enriched')}}
        
        group by order_id
),

join_totals_with_orders as (
    SELECT
        oit.order_id,
        oit.to
        customer_id, 
        order_date, 
        order_status,
        shipping_cost
)

