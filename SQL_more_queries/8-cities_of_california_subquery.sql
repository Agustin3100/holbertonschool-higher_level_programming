-- List all california elements
SELECT id, name FROM cities 
WHERE id = (SELECT *
	FROM states
	WHERE name = 'California');
