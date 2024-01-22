--find the first and latest order dates?

select 
	min(order_date) as min_order,
	max(order_date) as max_order
from orders