-- List all records of a table
SELECT score, name, COUNT(*)
FROM second_table
GROUP BY score, name ORDER BY score DESC;
