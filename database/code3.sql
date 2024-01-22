--order shpping to any countries within latin america

select * from orders
where ship_country in ('Brazil','Mexico','Argentina','Venezuela')
order by ship_country