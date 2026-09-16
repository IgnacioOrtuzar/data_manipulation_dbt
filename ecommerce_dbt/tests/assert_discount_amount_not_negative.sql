select *
from {{ ref('int_order_items_enriched') }}
where discount_amount < 0