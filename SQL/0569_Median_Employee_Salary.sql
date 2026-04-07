SELECT Id, Company, Salary
FROM (
    SELECT
        Id,
        Company,
        Salary,
        ROW_NUMBER() OVER (PARTITION BY Company ORDER BY Salary, Id) AS salary_rank,
        COUNT(*) OVER (PARTITION BY Company) AS total_count
    FROM Employee
) AS t
WHERE salary_rank BETWEEN (total_count + 1) / 2 AND (total_count + 2) / 2;
