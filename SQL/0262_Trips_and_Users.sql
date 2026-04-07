###Write your MySQL query statement below
select
    t.Request_at as Day,
    round(avg(case when t.Status = 'completed' then 0 else 1 end), 2) as `Cancellation Rate`
from Trips t
join Users c
    on t.Client_Id = c.Users_Id
    and c.Banned = 'No'
join Users d
    on t.Driver_Id = d.Users_Id
    and d.Banned = 'No'
where t.Request_at between '2013-10-01' and '2013-10-03'
group by t.Request_at
order by t.Request_at
