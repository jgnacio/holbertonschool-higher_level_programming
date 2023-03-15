-- Script that lists all shows contained in the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = show_id ORDER BY title, genre_id;