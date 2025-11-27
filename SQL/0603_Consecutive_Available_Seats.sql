# Write your MySQL query statement below
SELECT first.seat_id as seat_id
FROM Cinema first inner join Cinema second
WHERE first.free = True AND second.free = True AND (first.seat_id = second.seat_id + 1 OR first.seat_id = second.seat_id - 1)
GROUP BY 1