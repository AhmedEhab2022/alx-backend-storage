-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that
-- computes and store the average weighted score for all students.

-- Custom delimiter
DELIMITER $$

-- Create stored procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN

  -- Update the average score
  UPDATE users
  SET average_score = (SELECT (SUM(weight * score) / Sum(weight)), id
                      FROM corrections, projects, users
                      WHERE corrections.user_id = id
                      AND projects.id = project_id);

END$$

-- Reset delimiter
DELIMITER ;
