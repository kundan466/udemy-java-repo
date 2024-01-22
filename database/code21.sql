--get the highest,lowest,total and avg salary of all employees

select 
	ROUND(max(salary),2) as "Max salary",
	ROUND(min(salary),2) as "Min salary",
	ROUND(sum(salary),2) as "total salary",
	ROUND(avg(salary),2) as "Average salary"
from employees