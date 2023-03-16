-- Script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT name FROM tv_genres, tv_shows INNER JOIN tv_show_genres ON tv_shows.id = show_id WHERE title = 'Dexter' AND genre_id = tv_genres.id ORDER BY name;
