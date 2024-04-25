-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that
-- computes and store the average weighted score for all students.

-- Custom delimiter
DELIMITER $$

-- Create stored procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN

  -- Update the average score
  UPDATE users
  SET average_score = (SELECT (SUM(weight * score) / Sum(weight))
                      FROM corrections, projects
                      WHERE corrections.user_id = users.id
                      AND projects.id = project_id);

END$$

-- Reset delimiter
DELIMITER ;
