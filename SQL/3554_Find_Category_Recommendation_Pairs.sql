WITH users AS (
  SELECT DISTINCT
    a.user_id,
    LEAST(a.product_id, b.product_id) AS product_id1,
    GREATEST(a.product_id, b.product_id) AS product_id2
  FROM ProductPurchases a
  JOIN ProductPurchases b
    ON a.user_id = b.user_id
   AND a.product_id <> b.product_id
),
pair_info AS (
  SELECT DISTINCT
    u.product_id1,
    u.product_id2,
    LEAST(p1.category, p2.category) AS category1,
    GREATEST(p1.category, p2.category) AS category2
  FROM users u
  JOIN ProductInfo p1 ON p1.product_id = u.product_id1
  JOIN ProductInfo p2 ON p2.product_id = u.product_id2
)
SELECT
  pi.category1,
  pi.category2,
  COUNT(DISTINCT u.user_id) AS customer_count
FROM users u
JOIN pair_info pi
  ON pi.product_id1 = u.product_id1
 AND pi.product_id2 = u.product_id2
WHERE pi.category1 <> pi.category2
GROUP BY pi.category1, pi.category2
HAVING COUNT(DISTINCT u.user_id) >= 3
ORDER BY customer_count DESC, pi.category1, pi.category2;
