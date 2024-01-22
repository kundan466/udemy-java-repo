--list employees with late shipped orders
with late_orders as(select 
employee_id,count(*) as total_late_orders
from orders
where shipped_date>required_date
group by employee_id),
all_orders as(
select employee_id,
	count(*)as total_orders
from orders
group by employee_id)


select 
	employees.employee_id,
	employees.first_name,
	all_orders.total_orders,
	late_orders.total_late_orders
from employees
join all_orders on all_orders.employee_id=employees.employee_id
join late_orders on late_orders.employee_id=employees.employee_id
