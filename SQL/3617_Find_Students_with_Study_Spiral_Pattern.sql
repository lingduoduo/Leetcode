WITH eligible AS (
  SELECT
    student_id,
    SUM(hours_studied) AS total_study_hours,
    COUNT(DISTINCT subject) AS cycle_length,
    COUNT(*) AS session_cnt
  FROM study_sessions
  GROUP BY student_id
  HAVING COUNT(DISTINCT subject) >= 3
     AND COUNT(*) >= 6
),
cte AS (
  SELECT
    s.student_id,
    s.subject,
    s.session_date,
    e.total_study_hours,
    e.cycle_length,
    DATEDIFF(
      LEAD(s.session_date, 1, s.session_date) OVER (
        PARTITION BY s.student_id
        ORDER BY s.session_date
      ),
      s.session_date
    ) AS no_days
  FROM eligible e
  JOIN study_sessions s
    ON s.student_id = e.student_id
),
cte_rn AS (
  SELECT
    student_id,
    subject,
    total_study_hours,
    cycle_length,
    ROW_NUMBER() OVER (
      PARTITION BY student_id
      ORDER BY session_date
    ) AS rn
  FROM cte
  WHERE no_days < 3
),
cte2 AS (
  SELECT
    a.student_id,
    MAX(a.cycle_length) AS cycle_length,
    MAX(a.total_study_hours) AS total_study_hours
  FROM cte_rn a
  JOIN cte_rn b
    ON a.student_id = b.student_id
   AND b.rn = a.rn + a.cycle_length
   AND b.subject = a.subject
  GROUP BY a.student_id
  HAVING COUNT(DISTINCT a.subject) >= 3
)
SELECT
  st.student_id,
  st.student_name,
  st.major,
  c.cycle_length,
  c.total_study_hours
FROM cte2 c
JOIN students st
  ON st.student_id = c.student_id
ORDER BY c.cycle_length DESC, c.total_study_hours DESC;
