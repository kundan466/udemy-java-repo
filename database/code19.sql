--customers with multiple orders
--say within 4days period

with next_order_date as(
select 
	customer_id,order_date,lead(order_date,1)over(partition by customer_id order by customer_id,order_date) as next_order_date
	from orders
)
select
customer_id,order_date,next_order_date,
(next_order_date-order_date)as days_btw_orders
from next_order_date
where (next_order_date-order_date)<=4