--list top 5 highest freight charges in year 1997 

select
	ship_country,
	max(freight)
from orders
where order_date between ('1997-01-01') and ('1997-12-31')
group by ship_country
order by 2 desc
limit 5