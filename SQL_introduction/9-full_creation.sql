-- Exercise 9: Create a new table named 'second_table'.
-- If the table already exists, no error should occur.

-- the table should look like this:
-- id |   name   | score
--  1 |  "John"  |   10
--  2 |  "Alex"  |    3
--  3 |  "Bob"   |   14
--  4 | "George" |   18

CREATE TABLE IF NOT EXISTS second_table
(
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table VALUES (1, "John", 10);
INSERT INTO second_table VALUES (2, "Alex", 3);
INSERT INTO second_table VALUES (3, "Bob", 14);
INSERT INTO second_table VALUES (4, "George", 18);