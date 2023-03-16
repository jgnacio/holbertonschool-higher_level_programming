-- Script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT title, name FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = show_id LEFT JOIN tv_genres ON genre_id = tv_genres.id ORDER BY title;
