select *
from {{ ref('int_order_items_enriched') }}
where net_amount > gross_amount