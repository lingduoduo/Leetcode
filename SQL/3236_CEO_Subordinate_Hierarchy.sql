# Write your MySQL query statement below
WITH RECURSIVE
org AS (
  SELECT
    e.employee_id,
    e.manager_id,
    e.employee_name,
    e.salary,
    1 AS level,
    e.employee_id AS ceo_id,
    e.salary      AS ceo_salary
  FROM Employees e
  WHERE e.manager_id IS NULL

  UNION ALL

  SELECT
    e.employee_id,
    e.manager_id,
    e.employee_name,
    e.salary,
    o.level + 1,
    o.ceo_id,
    o.ceo_salary
  FROM Employees e
  JOIN org o
    ON e.manager_id = o.employee_id
)
SELECT
  employee_id   AS subordinate_id,
  employee_name AS subordinate_name,
  level - 1         AS hierarchy_level,
  salary - ceo_salary AS salary_difference
FROM org
WHERE manager_id IS NOT NULL
ORDER BY ceo_id, level, employee_id;
