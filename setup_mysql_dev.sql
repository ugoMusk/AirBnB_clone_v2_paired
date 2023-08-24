-- create database hbnb_dev_db if it does not exits
-- create user hbnb_dev with pwd hbnb_dev_pwd if it not exits
-- grant hbnb_dev select on performance_schema
-- grant all privileges on hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
