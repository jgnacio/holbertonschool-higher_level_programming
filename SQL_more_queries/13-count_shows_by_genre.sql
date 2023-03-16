-- Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT NAME AS genre, count(id) As number_of_shows FROM tv_genres INNER JOIN tv_show_genres ON genre_id = id GROUP BY genre ORDER BY number_of_shows DESC;
