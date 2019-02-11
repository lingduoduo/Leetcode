SELECT Id, Company, Salary
FROM Employee
WHERE 1 >= ABS(
	SELECT count(*) FROM Employee e1 WHERE e.company = e1.company AND e.Salary >= e1.Salary) -
	SELECT count(*) FROM Employee e2 WHERE e.company = e2.company AND e.Salary <= e1.Salary))
GROUP BY Company, Salary
