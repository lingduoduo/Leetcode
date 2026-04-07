SELECT IFNULL(
    ROUND(a.accepted_count / b.requested_count, 2),
    0
) AS accept_rate
FROM (
    SELECT COUNT(DISTINCT requester_id, accepter_id) AS accepted_count
    FROM RequestAccepted
) a
CROSS JOIN (
    SELECT COUNT(DISTINCT sender_id, send_to_id) AS requested_count
    FROM FriendRequest
) b;
