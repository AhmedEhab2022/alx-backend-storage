-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

SELECT band_name, (split - formed) As lifespan
FROM bands
WHERE style = 'Glam rock' AND split <= '2022'
GROUP BY band_name
ORDER BY lifespan DESC;
