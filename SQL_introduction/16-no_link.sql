-- List all records of a table
SELECT score, name, COUNT(*) AS number, COUNT(*) AS number
FROM second_table
GROUP BY score;
