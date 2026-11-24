
SELECT
    genre, COUNT(*)
FROM
    songs
GROUP BY
    genre;

SELECT
    genre, 
    COUNT(*), 
    CAST(AVG(duration) AS FLOAT) AS average_duration
FROM
    songs
GROUP BY
    genre;