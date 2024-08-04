SELECT Name
FROM Employee
JOIN (
	SELECT ManangerId
	FROM Employee
	GROUP BY ManangerId
	HAVING count(ManangerId) >= 5
) FREQ
ON Employee.Id = FREQ.ManangerId