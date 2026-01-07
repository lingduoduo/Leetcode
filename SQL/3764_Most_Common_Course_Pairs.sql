# Write your MySQL query statement below
WITH users AS (
    SELECT user_id
    FROM course_completions
    GROUP BY user_id
    HAVING COUNT(course_id) >= 5
       AND AVG(course_rating) >= 4
),

tbl AS (
    SELECT
        LAG(c.course_name) OVER (
            PARTITION BY c.user_id
            ORDER BY c.completion_date
        ) AS first_course,
        c.course_name AS second_course
    FROM course_completions c
    JOIN users u
      ON c.user_id = u.user_id
)

SELECT
    first_course,
    second_course,
    COUNT(*) AS transition_count
FROM tbl
WHERE first_course IS NOT NULL
GROUP BY first_course, second_course
ORDER BY transition_count DESC, first_course, second_course;
