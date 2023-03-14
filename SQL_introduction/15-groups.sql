-- Exercise 15: Display each INDIVIDUAL/distinct value
-- in the 'second_table' table, and how many times
-- it's trully present in the table.
  
-- (but only the score and number)
SELECT score, COUNT(score) AS number FROM second_table
    GROUP BY score
    ORDER BY score DESC;

-- (I THINK) the machine should look like this:
-- (Yes, SQL is Turing complete)

-- "FROM second_table":
-- score: 5, 3, 6, 3, 7

-- "SELECT score, COUNT(score) AS number":
-- score:  5, 3, 6, 3, 7
-- number: 1, 2, 1, 2, 1

-- "GROUP BY score"
-- score:  5, 3, 6, 7
-- number: 1, 2, 1, 1

-- "ORDER BY score DESC"
-- score:  7, 6, 5, 3
-- number: 1, 1, 1, 2