WITH ranked AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY event_date DESC, event_id DESC
        ) AS rn
    FROM subscription_events
),
user_stats AS (
    SELECT
        user_id,
        MAX(monthly_amount) AS max_historical_amount,
        MIN(event_date) AS first_event_date,
        MAX(event_date) AS last_event_date,
        MAX(CASE WHEN event_type = 'downgrade' THEN 1 ELSE 0 END) AS has_downgrade
    FROM subscription_events
    GROUP BY user_id
),
current_state AS (
    SELECT
        user_id,
        event_type AS current_event_type,
        plan_name AS current_plan,
        monthly_amount AS current_monthly_amount
    FROM ranked
    WHERE rn = 1
)
SELECT
    c.user_id,
    c.current_plan,
    c.current_monthly_amount,
    s.max_historical_amount,
    DATEDIFF(s.last_event_date, s.first_event_date) AS days_as_subscriber
FROM current_state c
JOIN user_stats s