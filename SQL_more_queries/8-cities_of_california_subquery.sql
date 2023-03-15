-- List all california elements
SELECT id, name FROM cities 
WHERE name = (SELECT id
	FROM states
	WHERE name = 'California');
