select count(*) as total_rows
from amazon_sales;

select * from amazon_sales
limit 5;

select count(*) as Total_Orders
from amazon_sales;

select round(sum(Amount),2)as Total_Sales
from amazon_sales;

select sum(QTY) as Total_Quantity
from amazon_sales;

select count(distinct Category)
as Total_Categories
from amazon_sales;

select Status,
count(*) as Orders
from amazon_sales
group by Status
order by Orders desc;

select ship_state,
round(sum(Amount),2) as Total_Sales
from amazon_sales
group by ship_state
order by Total_Sales desc
limit 10;

select ship_city,
round(sum(Amount),2) as Total_Sales
from amazon_sales
group by ship_city
order by Total_Sales desc
limit 10;


select Sales_Channel,
round(sum(Amount),2) as Revenue
from amazon_sales
group by Sales_Channel;

select round(avg(Amount),2) as Average_Order_Value
from amazon_sales;