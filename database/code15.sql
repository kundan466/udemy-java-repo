--lets get the details of the items too
with duplicate_entries as 
(
select order_id,quantity
from order_details
where quantity>60
group by order_id,quantity
having count(*)>1
order by order_id
)
select 
*
from order_details
where order_id in (select order_id from duplicates_entries)
order by order_id