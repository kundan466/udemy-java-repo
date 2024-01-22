--get the names ,salary and calculate 15% of salary for all employees

select first_name,last_name,salary,salary*.15 as salary_15per
from employees
order by 4 desc