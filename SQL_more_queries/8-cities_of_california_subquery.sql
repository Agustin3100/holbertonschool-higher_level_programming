-- List all california elements
SELECT id, name FROM cities 
WHERE EXISTS = (SELECT id
	FROM states
	WHERE name = 'California');
