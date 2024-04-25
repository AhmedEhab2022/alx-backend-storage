-- SQL script that creates a function SafeDiv that divides (and returns) the first by the second number
-- or returns 0 if the second number is equal to 0.

-- Custom delimiter
DELIMITER $$

-- Create function
CREATE FUNCTION SafeDiv(x INT, y INT)
-- Declare that the function returns integer and deterministic
RETURNS INT DETERMINISTIC
BEGIN
  IF y = 0 THEN
    RETURN 0;
  ELSE
    RETURN x / y;
  END IF;
END$$

-- Reset delimiter
DELIMITER ;
