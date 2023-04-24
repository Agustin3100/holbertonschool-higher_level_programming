#!/usr/bin/node
const listMovies = document.getElementById('list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const movieTitles = data.results.map(movie => movie.title);

    movieTitles.forEach(title => {
      const li = document.createElement('li');
      const textNode = document.createTextNode(title);
      li.appendChild(textNode);
      listMovies.appendChild(li);
    });
  })
  .catch(error => console.log(error));
