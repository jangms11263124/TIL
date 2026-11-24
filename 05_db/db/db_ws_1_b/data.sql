SELECT 
    title, artist, album
FROM 
    songs
ORDER BY
    title DESC;

SELECT 
    title, artist, album
FROM 
    songs
GROUP BY
    genre;

SELECT 
    title, artist, album
FROM 
    songs
WHERE
    duration >= 3;