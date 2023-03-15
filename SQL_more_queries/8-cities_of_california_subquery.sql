-- Exercise 8: list all the cities of California
-- The states table, when testing this script using
-- Holberton's checkers, will contain only one record
-- where name = California
-- (but the exact ids are not promise)
-- Results must be sorted in ascending order by
-- cities.id
-- Using the "JOIN" keyword is not allowed in this script.
-- (as a challenge)
SELECT id, name FROM cities
    WHERE state_id IN (
        SELECT id FROM states 
        WHERE states.name = "California"
    )
    ORDER BY id ASC;
-- A selection inside a selection just treats the previous
-- selection as a table, from what I can tell.
-- I chose to put "states.name" instead of just "name"
-- in fear of the wrong "name" column in the wrong table
-- being chosen. It seemed to work in my local server.