select *
from {{ ref('int_order_items_enriched') }}
where total_cost < 0