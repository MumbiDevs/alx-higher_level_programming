-- 100-not_my_genres.sql
SELECT DISTINCT tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.title != 'Dexter' OR tv_show_genres.title IS NULL
ORDER BY tv_genres.name ASC;
