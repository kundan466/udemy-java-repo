--orders shipping to usa or france

select * from orders
order by ship_country;

select* from orders 
where ship_country='USA' or ship_country='France'
