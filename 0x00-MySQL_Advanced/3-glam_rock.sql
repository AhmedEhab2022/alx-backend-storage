-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

SELECT band_name, (split - formed) AS lifespan
FROM bands
WHERE style = 'Glam rock' AND formed IS NOT NULL AND split IS NOT NULL
ORDER BY lifespan DESC;
