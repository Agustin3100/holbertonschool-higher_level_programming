-- List all california elements
SELECT ALL id, name FROM cities 
WHERE id = (SELECT id
	FROM states
	WHERE name = 'California');
