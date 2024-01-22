--list all employees with first_name starts with letters 'A','C' OR 'H'

select first_name
from employees
where first_name like'A%' or
	  first_name like'C%' or
	  first_name like'H%'
order by first_name
