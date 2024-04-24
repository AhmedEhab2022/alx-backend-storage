-- SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

-- Custom delimiter
DELIMITER $$

-- Create trigger
CREATE TRIGGER update_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  UPDATE items
  SET quantity = quantity - NEW.number
  WHERE items.name = NEW.item_name;
END$$

-- Reset delimiter
DELIMITER ;
