--first order from each country

with orders_by_country as
(
	select 
		ship_country,order_id,order_date,row_number()over(partition by ship_country order by ship_country,order_date) country_row_number
	from orders
)
select 
ship_country,order_id,order_date
from orders_by_country
where country_row_number=1