-- a script that lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT tv_shows.title, SUM(tv_shows_rating) AS 'rating'
FROM tv_shows
INNER JOIN tv_shows_rating
ON tv_shows.id = tv_shows_rating.show_id
GROUP BY title
ORDER BY rating DESC;