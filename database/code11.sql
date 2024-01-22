--customers with no orders
select
	*
from customers c
left join orders o on o.customer_id=c.customer_id
where o.customer_id is NULL