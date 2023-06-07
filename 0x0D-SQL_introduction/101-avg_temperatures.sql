-- Script that shows the average temperature
SELECT city, AVG(Value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
