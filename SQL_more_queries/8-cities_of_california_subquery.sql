-- List all california elements
SELECT id, name FROM cities 
WHERE id = (SELECT name
	FROM states
	WHERE name = 'California');
