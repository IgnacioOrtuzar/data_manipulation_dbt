select *
from {{ ref('fct_orders') }}
where total_gross_margin <> total_net_amount - complete_total_cost