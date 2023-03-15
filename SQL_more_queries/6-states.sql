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
    states (id INT NOT NULL, name VARCHAR(256));
