--query to get the difference between thr highest and lowest salary
--function:max,min and ?

select
	max(salary),
	min(salary),
	max(salary)-min(salary) as "difference"
from employees
group by job_id