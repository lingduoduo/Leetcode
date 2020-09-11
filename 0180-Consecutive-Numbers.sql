###Write your MySQL query statement below

SELECT distinct a.Num as ConsecutiveNums
FROM Logs a, Logs b, Logs c
WHERE a.Id = b.Id-1 and b.Id=c.Id-1
and a.Num = b.Num and b.Num = c.Num