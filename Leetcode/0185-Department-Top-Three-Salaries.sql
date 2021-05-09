###Write your MySQL query statement below
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
