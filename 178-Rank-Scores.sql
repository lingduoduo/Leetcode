# Write your MySQL query statement below
SELECT s.Score,
(SELECT count(distinct Score) from Scores where Score>= s.Score) Rank
FROM Scores s
ORDER BY s.Score desc


# Write your MySQL query statement below
select aa.Score, bb.Rank
from Scores aa
join (
    select a.Score, count(distinct b.Score) Rank
    from scores a, scores b
    where a.Score <= b.Score
    group by a.Score
) bb
on aa.Score = bb.Score
order by aa.Score desc