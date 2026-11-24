-- Active: 1777355348733@@127.0.0.1@3306
PRAGMA table_info('artists');

SELECT
    *
FROM
    artists;

SELECT
    count(*)
FROM
    artists;

SELECT
    ArtistId, Name
FROM
    artists
WHERE
    name in ('AC/DC')

SELECT
    Name
FROM
    artists;

SELECT
    ArtistId, Name
FROM
    artists
WHERE
    name in ('Gilberto Gil', 'Ed Motta')

SELECT
    ArtistId, Name
FROM
    artists
ORDER BY
    Name DESC;

SELECT
    ArtistId, Name
FROM
    artists
WHERE
    name LIKE 'Vinícius%' LIMIT 2;

SELECT
    ArtistId
FROM
    artists
WHERE
    ArtistId BETWEEN 50 AND 70;