#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

const characterId = '18'; // Wedge Antilles' character ID
let movieCount = 0;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
  } else {
    const films = JSON.parse(body).results;
    for (const film of films) {
      if (film.characters.includes(`https://swapi-api.hbtn.io/api/people/${characterId}/`)) {
        movieCount++;
      }
    }
    console.log(`${movieCount}`);
  }
});
