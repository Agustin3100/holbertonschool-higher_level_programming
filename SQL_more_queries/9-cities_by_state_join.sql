-- Display all ciSELECT DISTINCT cities.id, cities.name, states.name FROM cities, states
SELECT cities.id, cities.name, states.name FROM cities, states
GROUP BY cities.id, cities.name, states.name;
