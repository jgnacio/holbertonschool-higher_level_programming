-- script that creates the database hbtn_0d_usa and the table cities and
-- states_id references to id in the tables states.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE cities (id INT PRIMARY KEY AUTO_INCREMENT, states_id INT, name VARCHAR(256) NOT NULL, FOREIGN KEY (states_id) REFERENCES states(id));
