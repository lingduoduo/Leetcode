WITH tbl AS (
  SELECT
    id,
    month,
    salary,
    LAG(month, 1)  OVER (PARTITION BY id ORDER BY month) AS prev_m,
    LAG(salary, 1) OVER (PARTITION BY id ORDER BY month) AS prev_s,
    LAG(month, 2)  OVER (PARTITION BY id ORDER BY month) AS prev_m2,
    LAG(salary, 2) OVER (PARTITION BY id ORDER BY month) AS prev_s2,
    MAX(month) OVER (PARTITION BY id) AS max_month
  FROM Employee
)
SELECT
  id,
  month,
  salary
  + CASE WHEN prev_m  = month - 1 THEN prev_s  ELSE 0 END
  + CASE WHEN prev_m2 = month - 2 THEN prev_s2 ELSE 0 END AS Salary
FROM tbl
WHERE month != max_month
ORDER BY id, month DESC;
;
