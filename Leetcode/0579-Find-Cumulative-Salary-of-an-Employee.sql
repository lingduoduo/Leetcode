SELECT a.Id, MAX(b.Month) as Month, SUM(b.Salary) as Salary
FROM Employee a
JOIN Employee b
ON a.Id = b.Id
WHERE b.Month BETWEEN a.Month-3 and a.Month-1
GROUP BY a.Id, a.Month
ORDER BY a.Id, Month DESC
