--count total no of orders shipping to usa or france

select ship_country,count(*) from orders 
where ship_country='USA' or ship_country='France'
group by ship_country