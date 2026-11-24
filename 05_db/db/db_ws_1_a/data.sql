DROP TABLE songs;
PRAGMA table_info(songs);
SELECT * FROM songs;

CREATE TABLE songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    artist TEXT NOT NULL,
    album TEXT NOT NULL,
    genre TEXT NOT NULL,
    duration INTEGER NOT NULL
);

INSERT INTO 
    songs (title, artist, album, genre, duration)
VALUES
    ('404 NOT FOUND', '키키', '앨범', '댄스', 2);

INSERT INTO 
    songs (title, artist, album, genre, duration)
VALUES
    ('좋을텐데', '성시경', '앨범2', '발라드', 3);

INSERT INTO 
    songs (title, artist, album, genre, duration)
VALUES
    ('tipsy', 'ph-1', '앨범3', 'R&B', 4);

SELECT title, artist, album FROM songs;

UPDATE
    songs
SET 
    title = '페이지를 못찾음'
WHERE 
    id = 1;