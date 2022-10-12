-- Create a database and a user that is grant all privileges to the database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON 'hbnb_test_db' TO 'hbnb_test'@'localhost';
GRANT SELECT PRIVILEGE ON performance_schema TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;