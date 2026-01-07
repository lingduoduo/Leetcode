-- Write your MySQL query statement below
SELECT DISTINCT
    a.id,
    a.visit_date,
    a.people
FROM stadium a
CROSS JOIN stadium b
CROSS JOIN stadium c
WHERE
(
    (a.id = b.id - 1 AND a.id = c.id - 2) OR
    (a.id = b.id + 1 AND a.id = c.id - 1) OR
    (a.id = b.id + 2 AND a.id = c.id + 1)
)
AND a.people >= 100
AND b.people >= 100
AND c.people >= 100
ORDER BY a.visit_date;


WITH t AS (
  SELECT
    id, visit_date, people,
    LAG(people, 1) OVER (ORDER BY id) AS p1,
    LAG(people, 2) OVER (ORDER BY id) AS p2,
    LEAD(people, 1) OVER (ORDER BY id) AS n1,
    LEAD(people, 2) OVER (ORDER BY id) AS n2
  FROM stadium
)
SELECT id, visit_date, people
FROM t
WHERE people >= 100 AND (
      (p1 >= 100 AND p2 >= 100)
   OR (p1 >= 100 AND n1 >= 100)
   OR (n1 >= 100 AND n2 >= 100)
)
ORDER BY visit_date;
