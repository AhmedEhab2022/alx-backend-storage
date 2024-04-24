-- SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

-- Select origin and sum of fans from metal_bands
SELECT origin, SUM(fans) AS nb_fans
-- From metal_bands
FROM metal_bands
-- for each origin
GROUP BY origin
-- Order by number of fans in descending order
ORDER BY nb_fans DESC
