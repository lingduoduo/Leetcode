SELECT ifnull(Round(count(distinct request_id, accepter_id)/count(distinct sender_id, send_to_id), 2), 0) as accept_rate
FROM request_accepted, friend_request
