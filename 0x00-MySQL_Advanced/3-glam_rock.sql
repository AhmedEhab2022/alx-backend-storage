-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

SELECT band_name, (LEAST(2022, COALESCE(split, 2022)) - formed) AS lifespan
FROM bands
WHERE style = 'Glam rock' AND formed <= 2022
ORDER BY lifespan DESC;
