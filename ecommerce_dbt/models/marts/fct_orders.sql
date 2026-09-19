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

    select
        oit.order_id,
        o.customer_id,
        o.order_date,
        o.order_status,
        o.shipping_cost,

        oit.total_gross_amount,
        oit.total_discount_amount,
        oit.total_net_amount,
        oit.complete_total_cost,
        oit.total_gross_margin

    from order_item_totals as oit

    left join {{ ref('stg_orders') }} as o
        on oit.order_id = o.order_id
),

join_orders_total_with_order_payments as (

    select
        jtwo.*,
        op.failed_payment_count,
        op.payment_attempts,
        op.successful_payment_count,
        op.payment_successful,
        op.successful_amount,
        op.last_payment_date

    from join_totals_with_orders as jtwo

    left join {{ ref('int_order_payments') }} as op
        on jtwo.order_id = op.order_id

)


SELECT 
    *
FROM
    join_orders_total_with_order_payments

