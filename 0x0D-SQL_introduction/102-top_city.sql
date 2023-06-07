-- Script to get average temperature for three cities
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp  DESC LIMIT 3;
