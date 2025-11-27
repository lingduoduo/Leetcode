-- Write your MySQL query statement below
SELECT dept.name AS Department,
       empl.name AS Employee,
       empl.salary AS Salary
FROM Department dept
INNER JOIN Employee empl ON dept.id = empl.departmentId
WHERE empl.salary = (
    SELECT MAX(e.salary)
    FROM Employee e
    WHERE e.departmentId = dept.id
);

-- Write your MySQL query statement below
SELECT tbl.Department,
       tbl.Employee,
       tbl.Salary
FROM (
    SELECT dept.name AS Department,
           empl.name AS Employee,
           empl.salary AS Salary,
           RANK() OVER (PARTITION BY empl.departmentId ORDER BY empl.salary DESC) AS `rank`
    FROM Department dept
    INNER JOIN Employee empl ON dept.id = empl.departmentId
) tbl
WHERE tbl.`rank` = 1;