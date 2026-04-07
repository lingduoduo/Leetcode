SELECT ROUND(MIN(d), 2) AS shortest
FROM (
    SELECT SQRT(
        (p1.x - p2.x) * (p1.x - p2.x) +
        (p1.y - p2.y) * (p1.y - p2.y)
    ) AS d
    FROM Point2D p1
    JOIN Point2D p2
        ON p1.x < p2.x
        OR (p1.x = p2.x AND p1.y < p2.y)
) t;
