WITH RECURSIVE cte AS (
    SELECT giver_id, receiver_id, 1 AS len, gift_value
    FROM SecretSanta

    UNION ALL
    
    SELECT
        a.giver_id,
        b.receiver_id,
        a.len + 1 AS len,
        a.gift_value + b.gift_value AS gift_value
    FROM cte a
    JOIN SecretSanta b
      ON a.receiver_id = b.giver_id
    WHERE a.giver_id <> a.receiver_id
),
cycles AS (
    -- rows that "close" back to the start giver
    SELECT
        len AS chain_length,
        gift_value AS total_gift_value
    FROM cte
    WHERE giver_id = receiver_id
),
dedup AS (
    -- keep only one row per cycle signature (matches expected)
    SELECT DISTINCT chain_length, total_gift_value
    FROM cycles
)
SELECT
    DENSE_RANK() OVER (ORDER BY chain_length DESC, total_gift_value DESC) AS chain_id,
    chain_length,
    total_gift_value
FROM dedup
ORDER BY chain_id;
