-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

-- Select band_name and lifespan from bands
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
FROM bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
