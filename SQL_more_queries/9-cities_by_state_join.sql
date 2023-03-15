-- Display all cities
SELECT DISTINCT cities.id, cities.name, states.name FROM cities, states
INNER JOIN states
ORDER BY cities.id;
