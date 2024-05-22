-- Ensure the users exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant some basic privileges to user_0d_2 for demonstration purposes
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

-- List the privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- List the privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
