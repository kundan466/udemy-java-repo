--get all employees,and discard the last four characters from email

select first_name,email,length(email),substr(email,1,length(email)-4) as "extracted email"
from employees