-- This script shall list all rx of secondtable
SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;
