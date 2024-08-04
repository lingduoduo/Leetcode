# Write your MySQL query statement below
SELECT first.num AS ConsecutiveNums
FROM Logs first, Logs second, Logs third
WHERE first.id + 1 = second.id and second.id + 1 = third.id 
AND first.num = second.num and second.num = third.num
GROUP BY 1