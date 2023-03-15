-- Exercise 7: Create the new database 'hbtn_0d_usa'
-- and a table named 'cities' to it.
-- The 'cities' table's description should be similar to:
-- (id INT unique and auto generated and can't be NULL and is a PRIMARY KEY,
-- state_id INT, can't be NULL
-- and must be a FOREIGN KEY that references to 'id' of the 'states' table,
-- name VARCHAR(256))
-- If the database (inclusive)or the table already exists,
-- this script should not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS
cities
    (id INT AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256),
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id));
-- You can also define the constraints to keys
-- at the bottom, like this ^
-- At least, according to w3schools.com
