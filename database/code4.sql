--show order total amount per each order line

total amount=(unit_price*quantity)-discount

select order_id,product_id,unit_price,quantity,discount,
		((unit_price*quantity)-discount) as total_order_amount
from order_details;