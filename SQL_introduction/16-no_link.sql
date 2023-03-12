-- Exercise 16: Display all records in the 'second_table',
-- but only if they contain a 'name' value.
-- Display sorted by score, descending.
SELECT * FROM second_table ORDER BY score DESC
    WHERE score IS NOT NULL;
