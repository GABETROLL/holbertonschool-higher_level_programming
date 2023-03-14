-- Exercise 3: create a table 'force_name'.
-- Have its columns be: (id INT, name VARCHAR(256) can't be null)
-- If the table already exists, this script shouldn't fail.
CREATE TABLE IF NOT EXISTS
    force_name (id INT, name VARCHAR(256) NOT NULL);
