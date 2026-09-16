-- tests/assert_unsuccessful_orders_have_zero_amount.sql

select *
from {{ ref('int_order_payments') }}
where payment_successful = false
  and successful_amount <> 0