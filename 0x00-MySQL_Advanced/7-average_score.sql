-- SQL script that creates a stored procedure ComputeAverageScoreForUser that
-- computes and store the average score for a student.
-- Note: An average score can be a decimal

-- Custom delimiter
DELIMITER $$

-- Create stored procedure
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN

  -- Update the average score
  UPDATE users
  SET average_score = (SELECT AVG(score)
                      FROM corrections
                      WHERE projects.user_id = user_id)
  WHERE id = user_id;

END$$

-- Reset delimiter
DELIMITER ;
