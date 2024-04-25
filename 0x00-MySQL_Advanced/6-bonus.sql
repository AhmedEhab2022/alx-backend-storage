-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

-- Custom delimiter
DELIMITER $$

-- Create stored procedure
CREATE PROCEDURE AddBonus(IN user_id INT,
                          IN project_name VARCHAR(255),
                          IN score INT)
BEGIN
  -- DECLARE project_id
  DECLARE project_id INT;

  -- Add the project if it does not exist
  IF project_id IS NULL THEN
    INSERT INTO projects(name)
    VALUES (project_name);
  END IF;

  -- STORE project_id
  SELECT id INTO project_id
  FROM projects
  WHERE name = project_name;

  -- Add the correction
  INSERT INTO corrections(user_id, project_id, score)
  VALUES (user_id, project_id, score);

END$$

-- Reset delimiter
DELIMITER ;
