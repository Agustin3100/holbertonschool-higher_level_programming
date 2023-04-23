#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
