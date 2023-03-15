-- Display all cities
SELECT cities.id, cities.name, states.name FROM cities, states
ORDER BY cities.id;
