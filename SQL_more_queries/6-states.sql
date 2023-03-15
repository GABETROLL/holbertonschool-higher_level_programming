-- Exercise 6: Create a new database called 'hbtn_0d_usa'.
-- In this database, create the table 'states',
-- that has these columns:
-- (id INT, unique, auto generated, can't be NULL and is a primary key,
-- name VARCHAR(256) can't be null)
-- If the table (inclusive)or the database don't exist,
-- this script shouldn't fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa; -- <--
CREATE TABLE IF NOT EXISTS
    states (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256));
-- (according to w3schools.com) "PRIMARY KEY" does the same thing as
-- "NOT NULL UNIQUE", and "UNIQUE" means the value
-- can't repeat other values in the same column.

-- (Also, according to w3schools.com):
-- "AUTO_INCREMENT" can be used to auto-generate
-- a new, unique number whenever a record is added.
-- (It starts at 1 and increments by 1 for each new record)
