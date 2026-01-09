WITH RECURSIVE
org AS (
  -- anchor: top-level manager(s)
  SELECT
    e.employee_id,
    e.manager_id,
    e.employee_name,
    e.salary,
    1 AS level
  FROM Employees e
  WHERE e.manager_id IS NULL

  UNION ALL

  -- walk down the hierarchy
  SELECT
    e.employee_id,
    e.manager_id,
    e.employee_name,
    e.salary,
    o.level + 1
  FROM Employees e
  JOIN org o
    ON e.manager_id = o.employee_id
),
tree AS (
  -- each employee is an ancestor of themself
  SELECT
    e.employee_id AS ancestor_id,
    e.employee_id AS descendant_id
  FROM Employees e

  UNION ALL

  -- expand descendants
  SELECT
    t.ancestor_id,
    e.employee_id AS descendant_id
  FROM tree t
  JOIN Employees e
    ON e.manager_id = t.descendant_id
)
SELECT
  o.employee_id,
  o.employee_name,
  o.level,
  SUM(CASE WHEN t.descendant_id <> o.employee_id THEN 1 ELSE 0 END) AS team_size,
  SUM(e2.salary) AS budget
FROM org o
JOIN tree t
  ON t.ancestor_id = o.employee_id
JOIN Employees e2
  ON e2.employee_id = t.descendant_id
GROUP BY o.employee_id, o.employee_name, o.level
ORDER BY o.level, budget DESC, o.employee_name;
