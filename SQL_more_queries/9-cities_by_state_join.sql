-- Display all cities
SELECT COUNT(DISTINCT cities.id, cities.name, states.name) FROM cities, states
ORDER BY cities.id;
