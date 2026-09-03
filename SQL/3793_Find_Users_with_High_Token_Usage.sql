SELECT user_id, 
    COUNT(prompt) prompt_count,
    ROUND(AVG(tokens), 2) avg_tokens
FROM PROMPTs
GROUP BY 1
HAVING prompt_count >= 3 and MAX(tokens) > avg_tokens
ORDER BY avg_tokens DESC, USER_ID
