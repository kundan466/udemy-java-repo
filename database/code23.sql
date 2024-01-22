--query to lowest-paid salary paid by each manager_id
select manager_id,min(salary),salary
from employees
where manager_id is not null
and manager_id!=0