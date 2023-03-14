-- Exercise 0: list the users'
-- (user_0d_1 and user_0d_2)'s privileges.

-- From what I understand, "the SQL server"
-- is running in 'localhost', which is the
-- machine that's running the server and
-- this script.
SHOW GRANTS FOR user_0d_1@localhost;
-- second one
SHOW GRANTS FOR user_0d_2@localhost;
