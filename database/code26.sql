--query to list max salary of each point for max salary is at or above 5000dollars

select job_id,
	max(salary)
from employees
group by job_id
having max(salary)>5000