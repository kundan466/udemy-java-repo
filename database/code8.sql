--list top 5 heighest freight chargers

select
	ship_country,
	max(freight)
from orders
group by ship_country
order by 2 desc
limit 5