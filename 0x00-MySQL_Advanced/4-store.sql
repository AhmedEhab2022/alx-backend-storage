-- SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

-- Create trigger
CREATE TRIGGER update_quantity
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - orders.number
WHERE items.name = orders.item_name;
