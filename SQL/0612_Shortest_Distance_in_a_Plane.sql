SELECT ROUND(MIN(d), 2) AS shortest
FROM (
  SELECT
    SQRT((f.x - s.x) * (f.x - s.x) + (f.y - s.y) * (f.y - s.y)) AS d
  FROM Point2D f
  JOIN Point2D s
  WHERE (f.x, f.y) != (s.x, s.y)
) t;