-- 14-my_genres.sql
SELECT tv_genres.name
FROM tv_show_genres
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows ON tv_show_genres.title = tv_shows.title
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
