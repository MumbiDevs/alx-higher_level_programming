-- 13-count_shows_by_genre.sql
SELECT tv_show_genres.genre AS genre, COUNT(tv_shows.title) AS number_of_shows
FROM tv_shows
JOIN tv_show_genres ON tv_shows.title = tv_show_genres.title
GROUP BY tv_show_genres.genre
ORDER BY number_of_shows DESC;
