-- 101-not_a_comedy.sql
SELECT DISTINCT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.title = tv_show_genres.title
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name != 'Comedy' OR tv_genres.name IS NULL
ORDER BY tv_shows.title ASC;
