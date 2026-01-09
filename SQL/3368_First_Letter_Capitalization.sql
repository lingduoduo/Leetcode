WITH RECURSIVE words AS (
  SELECT
    content_id,
    content_text,
    1 AS pos,
    TRIM(SUBSTRING_INDEX(content_text, ' ', 1)) AS word,
    TRIM(SUBSTRING(content_text, LENGTH(SUBSTRING_INDEX(content_text, ' ', 1)) + 1)) AS rest
  FROM user_content

  UNION ALL

  SELECT
    content_id,
    content_text,
    pos + 1,
    TRIM(SUBSTRING_INDEX(rest, ' ', 1)) AS word,
    TRIM(SUBSTRING(rest, LENGTH(SUBSTRING_INDEX(rest, ' ', 1)) + 1)) AS rest
  FROM words
  WHERE rest IS NOT NULL AND rest <> ''
),
titled AS (
  SELECT
    content_id,
    content_text,
    pos,
    CASE
      WHEN word = '' THEN ''
      WHEN '-' in word upperword(split(word)) concat by '-'
      ELSE CONCAT(UPPER(SUBSTRING(word, 1, 1)), LOWER(SUBSTRING(word, 2)))
    END AS new_word
  FROM words
)
SELECT
  content_id,
  content_text original_text,
  TRIM(GROUP_CONCAT(new_word ORDER BY pos SEPARATOR ' ')) AS converted_text    
FROM titled
GROUP BY content_id, content_text;
