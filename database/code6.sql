--total products in each categories

select
	c.category_name,
	count(*) as total_products
from products p
inner join categories c on c.category_id=p.category_id
group by 1
order by 2 desc