-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

-- Select band_name and lifespan from bands
SELECT band_name, (LEAST(2022, COALESCE(split, 2022)) - formed) AS lifespan
FROM bands
WHERE style = 'Glam rock' AND formed <= 2022
ORDER BY lifespan DESC;
