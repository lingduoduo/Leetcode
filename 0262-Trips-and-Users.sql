###Write your MySQL query statement below
select a.Request_at as Day, 
round(sum(case when a.Status like 'complete%' then 0 else 1 end)/count(*),2) as 'Cancellation Rate'
from Trips a
join Users b
on a.Client_Id = b.Users_Id
join Users c
on a.Driver_Id = c.Users_Id
where a.Request_at between '2013-10-01' and '2013-10-03'
and b.Banned = "No"
and c.Banned = "No"
group by a.Request_at