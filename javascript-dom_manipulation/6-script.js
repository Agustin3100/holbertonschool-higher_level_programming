#!/usr/bin/node
const characterElement = document.getElementById('character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    const characterName = data.name;

    characterElement.textContent = characterName;
  })
  .catch(error => console.log(error));
