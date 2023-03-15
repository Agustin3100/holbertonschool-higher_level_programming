-- List all california elements
SELECT id, name FROM cities 
WHERE id = (SELECT id
	FROM states
	WHERE name = 'California');
