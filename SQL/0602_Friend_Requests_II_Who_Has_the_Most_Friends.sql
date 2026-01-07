# Write your MySQL query statement below
with tbl as (
select requester_id id, count(*) as cnt
from RequestAccepted
group by requester_id
union all
select accepter_id id, count(*) as cnt
from RequestAccepted
group by accepter_id
)

select id, sum(cnt) num
from tbl
group by 1
order by 2 desc
limit 1
