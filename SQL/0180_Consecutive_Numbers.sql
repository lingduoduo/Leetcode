-- # Write your MySQL query statement below
SELECT first.num AS ConsecutiveNums
FROM Logs first, Logs second, Logs third
WHERE first.id + 1 = second.id and second.id + 1 = third.id 
AND first.num = second.num and second.num = third.num
GROUP BY 1

SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num,
           LEAD(num, 1) OVER (ORDER BY id) AS next1,
           LEAD(num, 2) OVER (ORDER BY id) AS next2
    FROM Logs
) t
WHERE num = next1
  AND num = next2;