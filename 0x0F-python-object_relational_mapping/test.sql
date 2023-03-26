-- Database + tables to test
DROP DATABASE IF EXISTS test_13;
CREATE DATABASE IF NOT EXISTS test_13;
USE test_13;

CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("Illinois"), ("Arizona"), ("Texs"), ("New York");
