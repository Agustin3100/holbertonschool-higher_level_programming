-- Display all ciSELECT DISTINCT cities.id, cities.name, states.name FROM cities, states
SELECT UNIQUE cities.id, cities.name, states.name FROM cities, states
ORDER BY cities.id;
