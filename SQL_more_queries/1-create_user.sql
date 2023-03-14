-- Exercise 1: Create a new user called 'user_0d_1'.
-- with all privileges, 'user_0d_1_pwd'.
-- If the user 'user_0d_1' already exists, this script
-- shouldn't fail.
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- (creating user first, then granting it privileges)
GRANT ALL PRIVILEGES ON * TO 'user_0d_1'@'localhost'
    WITH GRANT OPTION;
-- (using "GRANT * ON *" will only grant 'USAGE',
-- according to what I'm seeing in the Holberton checkers)
