###Write your MySQL query statement below
select a.id, min(a.visit_date) visit_date, min(a.people) people
from stadium a
join stadium b 
join stadium c 
where 
((a.id = b.id-1 and a.id = c.id -2) or
(a.id = b.id+1 and a.id = c.id -1) or
(a.id = b.id+2 and a.id = c.id +1))
and a.people >=100
and b.people >=100
and c.people >=100
group by a.id
