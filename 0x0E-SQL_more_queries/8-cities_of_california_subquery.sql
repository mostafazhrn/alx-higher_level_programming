-- This script shall list cites of californias in db
SELECT id, name
FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California');
