-- Count number of genres
SELECT tv_genres.name COUNT(tv_show_genres.id) FROM tv_genres INNER JOIN tv_show_genres ON tv_show_genres.id = tv_show.id; 
