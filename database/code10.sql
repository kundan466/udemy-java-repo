--list top 5 highest freight charges last year

select
	ship_country,
	max(freight)
from orders
where 
	Extract('Y' from order_date)>=extract('Y' from(select max(order_date) from orders)) 
group by ship_country
order by 2 desc
limit 5