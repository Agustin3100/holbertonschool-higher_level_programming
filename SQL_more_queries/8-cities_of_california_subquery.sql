-- List all california elements
SELECT id, name FROM cities 
WHERE EXISTS id = (SELECT id
	FROM states
	WHERE name = 'California');
