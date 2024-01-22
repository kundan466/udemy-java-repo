--countries with customers or suppliers
select country 
from customers

union all

select country
from suppliers order by country