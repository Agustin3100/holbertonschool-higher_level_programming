-- List all california elements
SELECT id, name FROM cities 
WHERE id = (SELECT id, name
	FROM states
	WHERE name = 'California');
