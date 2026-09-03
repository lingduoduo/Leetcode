WITH valid_days AS (
    SELECT
        user_id,
        action_date,
        MAX(action) AS action
    FROM activity
    GROUP BY user_id, action_date
    HAVING COUNT(*) = 1
),
numbered AS (
    SELECT
        user_id,
        action_date,
        action,
        ROW_NUMBER() OVER (
            PARTITION BY user_id, action
            ORDER BY action_date
        ) AS rn
    FROM valid_days
),
streaks AS (
    SELECT
        user_id,
        action,
        COUNT(*) AS streak_length,
        MIN(action_date) AS start_date,
        MAX(action_date) AS end_date
    FROM numbered
    GROUP BY
        user_id,
        action,
        DATE_SUB(action_date, INTERVAL rn DAY)
),
ranked AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY streak_length DESC, start_date ASC
        ) AS rank_num
    FROM streaks
    WHERE streak_length >= 5
)
SELECT
    user_id,
    action,
    streak_length,
    start_date,
    end_date
FROM ranked
WHERE rank_num = 1
ORDER BY
    streak_length DESC,
    user_id ASC;