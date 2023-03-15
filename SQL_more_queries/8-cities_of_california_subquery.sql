-- List all california elements
SELECT id, name FROM cities 
WHERE = 
SELECT name
FROM states
WHERE name = 'California'
ORDER BY id;
