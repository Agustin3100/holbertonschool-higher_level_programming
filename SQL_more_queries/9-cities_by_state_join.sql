-- Display all cities
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.name=states.name
ORDER BY id;
