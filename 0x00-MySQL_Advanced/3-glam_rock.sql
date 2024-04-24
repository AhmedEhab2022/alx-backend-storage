-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

SELECT band_name, (2022 - formed) As lifespan
FROM bands
WHERE style = 'Glam rock'
GROUP BY band_name
ORDER BY lifespan DESC;
