-- List all records of a table
SELECT score, name, COUNT(*) AS ''
FROM second_table
WHERE name IS NOT NULL
GROUP BY score, name ORDER BY score DESC;
