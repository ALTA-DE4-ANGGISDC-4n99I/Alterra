slect 
order_id::int as orders_id
, order_date::timestimp as order_at
, customer_phone 
from {{ source('store', 'orders') }}