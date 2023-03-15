-- Display all cities
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.name=states.name
ORDER BY cities.idid;
