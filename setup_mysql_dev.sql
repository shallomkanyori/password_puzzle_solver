-- script that prepares a MySQL server
-- creates a database and a user

CREATE DATABASE IF NOT EXISTS pwd_solver_dev_db;
CREATE USER IF NOT EXISTS 'pwd_solver_dev'@'localhost' IDENTIFIED BY 'pwd_solver_dev_pwd';
GRANT ALL PRIVILEGES ON pwd_solver_dev_db.* TO 'pwd_solver_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'pwd_solver_dev'@'localhost';
FLUSH PRIVILEGES;
