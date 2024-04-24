-- SQL script that creates a table users with the following columns:
-- id: integer, primary key, auto increment
-- email: string, not null, unique
-- name: string

-- Create table users schema
CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255)
);
