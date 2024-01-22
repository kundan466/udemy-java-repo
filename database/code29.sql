--query to get the job_id and all the employees id within each job_id group

select job_id,array_agg(employee_id)
from employees
group by job_id