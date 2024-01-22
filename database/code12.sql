--top customers with their total order amount spend


select 
	c.customer_id,
	c.company_name,
	sum((od.unit_price*od.quantity)-od.discount) as total_amount
from customers c
join orders o on o.customer_id=c.customer_id
join order_details od on od.order_id=o.order_id
group by c.customer_id,c.company_name
order by 3 desc
limit 10