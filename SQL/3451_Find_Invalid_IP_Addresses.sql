WITH
cte_invalid_ip AS (
  SELECT log_id, ip
  FROM logs
  WHERE NOT REGEXP_LIKE(
    ip,
    '^(?:0|[1-9]\\d?|1\\d\\d|2[0-4]\\d|25[0-5])(?:\\.(?:0|[1-9]\\d?|1\\d\\d|2[0-4]\\d|25[0-5])){3}$'
  )
),
cte_invalid_ip_count AS (
  SELECT ip, COUNT(*) AS invalid_count
  FROM cte_invalid_ip
  GROUP BY ip
)
SELECT ip, invalid_count
FROM cte_invalid_ip_count
ORDER BY invalid_count DESC, ip DESC;
