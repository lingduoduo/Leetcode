# Write your MySQL query statement below
select a.Name as Customers
from Customers a
left join Orders b
on a.Id = b.CustomerId
where b.CustomerId is Null