-- Script to display count of scores
SELECT score,count(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
