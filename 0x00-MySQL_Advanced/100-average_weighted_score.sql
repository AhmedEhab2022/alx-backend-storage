-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.

-- Custom delimiter
DELIMITER $$

-- Create stored procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN

  -- Update the average score
  UPDATE users
  SET average_score = (SELECT (SUM(weight * score) / Sum(weight))
                      FROM corrections, projects
                      WHERE corrections.user_id = user_id
                      AND projects.id = project_id)
  WHERE id = user_id;

END$$

-- Reset delimiter
DELIMITER ;
