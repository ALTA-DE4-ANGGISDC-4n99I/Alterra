select
order_details_id:: int as order_details_id
, product_id::int as order_id
, product_id::int as product_id
, quantity as order_qty
, price as unit_sales
from{{ source ('store', 'orders_details')}}