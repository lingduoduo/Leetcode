###Write your MySQL query statement below
select a.Id
from Weather a 
inner join Weather b
where To_Days(a.RecordDate) = To_Days(b.RecordDate) + 1
and a.Temperature>b.Temperature