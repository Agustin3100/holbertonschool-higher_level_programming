-- Count number of genres
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows FROM tv_genres 
INNER JOIN tv_show genres 
ON tv_show_genres.show_id = tv_genres.id 
GROUP BY number_of_shows; 
