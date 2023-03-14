-- Exercise 2: Create a database 'hbtn_0d_2'.
-- Create the user 'user_0d_2' with password 'user_0d_2_pwd'.
-- Grant user 'user_0d_2' SELECT privilege in
-- the database 'hbtn_0d_2'.
-- If the database 'hbtn_0d_2' already exists,
-- (inclusive)or the user 'user_0d_2' doesn't exist,
-- this script shouldn't fail.

-- create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grant SELECT privilege
GRANT SELECT ON 'hbtn_0d_2'.* TO 'user_0d_2'@'localhost';
