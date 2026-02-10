WITH
user_cnt AS (
  SELECT user_id, COUNT(*) AS cnt
  FROM MovieRating
  GROUP BY user_id
),
top_user AS (
  SELECT u.name AS results
  FROM user_cnt c
  JOIN Users u ON u.user_id = c.user_id
  ORDER BY c.cnt DESC, u.name ASC
  LIMIT 1
),
movie_avg AS (
  SELECT movie_id, AVG(rating) AS avg_rating
  FROM MovieRating
  WHERE created_at >= '2020-02-01'
    AND created_at <  '2020-03-01'
  GROUP BY movie_id
),
top_movie AS (
  SELECT m.title AS results
  FROM movie_avg a
  JOIN Movies m ON m.movie_id = a.movie_id
  ORDER BY a.avg_rating DESC, m.title ASC
  LIMIT 1
)
SELECT results FROM top_user
UNION ALL
SELECT results FROM top_movie;
