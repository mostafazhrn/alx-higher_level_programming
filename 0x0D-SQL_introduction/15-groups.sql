-- this script shall list all num of rx with same score in tb
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score ORDER BY score DESC;
