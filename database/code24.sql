--avg salary for each department with more than 10 employees

select department_id,
ROUND(avg(salary),0),
count(*) as "total_employees"
from employees 
group by department_id
order by 3 desc