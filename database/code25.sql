--query to get avg salary for each post excluding programmer(IT_PROG)
select
	job_id,
	avg(salary)
from employees
where job_id<>'IT_PROG'
group by job_id