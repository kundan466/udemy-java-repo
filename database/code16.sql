--list all late shipped orders
select 
*
from orders
where shipped_date>required_date