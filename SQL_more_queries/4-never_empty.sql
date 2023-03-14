-- Exercise 4: Create a new table named 'id_not_null'
-- its description should be: 
-- (id INT with the default value 1,
-- name VARCHAR(256))
CREATE TABLE IF NOT EXISTS id_not_null
    (id INT DEFAULT 1, name VARCHAR(256));
