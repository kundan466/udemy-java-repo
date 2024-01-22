--orders with many line of items

select 
	order_id,
	count(*)
from order_details
group by order_id
order by 2 desc
limit 10