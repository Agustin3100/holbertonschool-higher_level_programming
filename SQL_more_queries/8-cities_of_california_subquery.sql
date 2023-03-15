-- List all california elements
SELECT id, name FROM cities 
WHERE state = (SELECT name
	FROM states
	WHERE name = 'California');
