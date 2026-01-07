WITH session AS (
  SELECT
    session_id,
    user_id,

    ROUND(
      TIMESTAMPDIFF(
        MINUTE,
        MIN(event_timestamp) OVER (PARTITION BY session_id, user_id),
        MAX(event_timestamp) OVER (PARTITION BY session_id, user_id)
      ),
      0
    ) AS session_duration_minutes,

    SUM(CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END)
      OVER (PARTITION BY session_id, user_id) AS scroll_cnt,

    SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END)
      OVER (PARTITION BY session_id, user_id) AS click_cnt,

    SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END)
      OVER (PARTITION BY session_id, user_id) AS purchase_cnt
  FROM app_events
),
session_metrics AS (
  SELECT DISTINCT
    session_id,
    user_id,
    session_duration_minutes,
    scroll_cnt,
    click_cnt,
    purchase_cnt,
    (click_cnt / CAST(scroll_cnt AS DECIMAL(18,6))) AS ratio
  FROM session
)
SELECT
  session_id,
  user_id,
  session_duration_minutes,
  scroll_cnt AS scroll_count
FROM session_metrics
WHERE session_duration_minutes > 30.0
  AND scroll_cnt >= 5
  AND ratio < 0.2
  AND purchase_cnt = 0
ORDER BY scroll_count DESC, session_id;
