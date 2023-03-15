-- List all california elements
SELECT id, name FROM cities 
WHERE EXISTS  
	(SELECT name
	FROM states
	WHERE name = 'California');
