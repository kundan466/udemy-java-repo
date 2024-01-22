--orders with double entry line items(qty>60)

select 
	order_id,quantity
from order_details
where quantity>60
group by order_id,quantity
having count(*)>1
order by order_id