SELECT Id, Company, Salary
WITH add_rank AS
    (SELECT id, company, salary,
        ROW_NUMBER()OVER(PARTITION BY company ORDER BY salary) AS rnk
    FROM Employee)
, add_count AS
    (SELECT company, COUNT(DISTINCT id) AS cnt
    FROM Employee
    GROUP BY company)
SELECT a.id, a.company, a.salary
FROM add_rank a
JOIN add_count b
ON a.company = b.company
AND a.rnk BETWEEN b.cnt / 2 AND b.cnt / 2 + 1

select Id, Company, Salary
from (select id, company, salary, 
			 row_number() over(partition by company order by salary) salaryrank, 
			 count(*) over(partition by company) tte 
	  from employee) as foo
where salaryrank >= tte/2 and salaryrank <= tte/2+1