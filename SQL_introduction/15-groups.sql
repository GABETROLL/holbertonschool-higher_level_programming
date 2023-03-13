-- Exercise 15: Display each INDIVIDUAL/distinct value
-- in the 'second_table' table, and how many times
-- it's trully present in the table.

-- (but only the score and number)
SELECT DISTINCT score, COUNT(DISTINCT score) FROM second_table;
