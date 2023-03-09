-- Exercise 4: Create a new table called "first_table"
-- the table must have those exact type descriptions
-- If the table doesn't exist, an error shouldn't occur.
-- Using "SELECT" or "SHOW" commands are not allowed.

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));