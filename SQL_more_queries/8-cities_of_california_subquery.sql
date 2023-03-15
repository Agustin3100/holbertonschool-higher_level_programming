-- List all california elements
SELECT id, name FROM cities 
WHERE name = (SELECT name
	FROM states
	WHERE name = 'California');
