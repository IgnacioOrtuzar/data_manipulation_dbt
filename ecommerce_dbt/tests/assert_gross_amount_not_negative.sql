select *
from {{ ref('int_order_items_enriched') }}
where gross_amount < 0