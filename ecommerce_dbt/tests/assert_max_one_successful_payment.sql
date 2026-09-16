-- tests/assert_max_one_successful_payment.sql

select *
from {{ ref('int_order_payments') }}
where successful_payment_count > 1