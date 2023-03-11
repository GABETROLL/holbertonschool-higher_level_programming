-- Exercise 11: list all records in the table 'second_table'.
-- Only show the score and name columns, in that order.
-- Records should be ordered by score, highest first.
-- Only records with a score higher than 10 can be displayed.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
