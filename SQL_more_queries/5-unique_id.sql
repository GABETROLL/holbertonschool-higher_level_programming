-- Exercise 5: create a new table named 'unique_id'.
-- The table's description should be:
-- (id INT with the default value 1 and must be unique,
-- name VARCHAR(256))
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1, VARCHAR(256));
