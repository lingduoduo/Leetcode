SELECT Candidate.Name
FROM Candidate
JOIN
(
	SELECT CandidateId
	FROM Vote
	GROUP BY CandidateId
	ORDER BY Count(*) DESC
	LIMIT 1
) MAX
ON Candidate.id = MAX.CandidateId
