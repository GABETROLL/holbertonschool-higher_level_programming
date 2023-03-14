-- Exercise 16: Display all records in the 'second_table',
-- but only if they contain a 'name' value.
-- Display sorted by score, descending.
SELECT (score, name) FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
