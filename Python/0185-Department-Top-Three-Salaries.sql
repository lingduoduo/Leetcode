--- Write your MySQL query statement below
SELECT D.Name as Department,
E.Name as Employee,
E.Salary
FROM Department D,
Employee E,
Employee E2
WHERE D.ID = E.DepartmentId
AND E.DepartmentId = E2.DepartmentId 
AND E.Salary <= E2.Salary
GROUP by D.ID, E.Name 
HAVING count(distinct E2.Salary) <= 3
ORDER by D.Name, E.Salary desc

SELECT tbl.Department,
       tbl.Employee,
       tbl.Salary
FROM (
    SELECT dept.name AS Department,
           empl.name AS Employee,
           empl.salary AS Salary,
           DENSE_RANK() OVER (PARTITION BY empl.departmentId ORDER BY empl.salary DESC) AS `rank`
    FROM Department dept
    INNER JOIN Employee empl ON dept.id = empl.departmentId
) tbl
WHERE tbl.`rank` <= 3
ORDER by 3;