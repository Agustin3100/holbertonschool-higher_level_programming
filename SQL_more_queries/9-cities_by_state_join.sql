-- Display all cities
SELECT id, name, states.name FROM cities, states
ORDER BY cities.id;
