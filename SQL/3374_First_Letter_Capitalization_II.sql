WITH RECURSIVE
cte AS (
  SELECT
    content_id,
    content_text,
    -- mimic REPLACE(content_text,'-','  ')
    REPLACE(content_text, '-', '  ') AS new_text
  FROM user_content
),
tokens AS (
  -- split new_text by spaces into ordered tokens
  SELECT
    content_id,
    content_text,
    new_text,
    1 AS pos,
    SUBSTRING_INDEX(new_text, ' ', 1) AS token,
    SUBSTRING(new_text, LENGTH(SUBSTRING_INDEX(new_text, ' ', 1)) + 2) AS rest
  FROM cte

  UNION ALL

  SELECT
    content_id,
    content_text,
    new_text,
    pos + 1,
    SUBSTRING_INDEX(rest, ' ', 1) AS token,
    SUBSTRING(rest, LENGTH(SUBSTRING_INDEX(rest, ' ', 1)) + 2) AS rest
  FROM tokens
  WHERE rest IS NOT NULL AND rest <> ''
),
cte2 AS (
  SELECT
    content_id,
    content_text,
    pos,
    CASE
      -- empty token means it came from the double-space placeholder => turn back into '-'
      WHEN token = '' THEN '-'
      ELSE CONCAT(UPPER(LEFT(token, 1)), LOWER(SUBSTRING(token, 2)))
    END AS converted
  FROM tokens
)
SELECT
  content_id,
  content_text AS original_text,
  -- join tokens with spaces, then collapse " - " back to "-"
  REPLACE(TRIM(GROUP_CONCAT(converted ORDER BY pos SEPARATOR ' ')), ' - ', '-') AS converted_text
FROM cte2
GROUP BY content_id, content_text
ORDER BY content_id;
