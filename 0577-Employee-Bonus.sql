SELECT e.name, b.bonus
FROM EMPLOYEE e
LEFT JOIN Bonus b
ON e.empID = b.empID
WHERE b.bonus<=1000 or b.bonus is NULL