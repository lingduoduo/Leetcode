SELECT r.question_id as survey_log
FROM (
	SELECT question_id, 
	SUM(case when action='SHOW' THEN 1 ELSE 0 END) show,
	SUM(case when action='ANSWER' THEN 1 ELSE 0 END) answer
) r
ORDER BY answer/show desc 
LIMIT 1
