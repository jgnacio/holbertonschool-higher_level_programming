-- Script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT title FROM tv_genres, tv_shows INNER JOIN tv_show_genres ON tv_shows.id = show_id WHERE name = 'Comedy' AND genre_id = tv_genres.id ORDER BY title;
