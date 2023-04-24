#!/usr/bin/node

const helloElement = document.getElementById('hello');

fetch('https://stefanbohacek.com/hellosalut/?lang=fr')
  .then(response => response.text())
  .then(data => {
    helloElement.textContent = data;
  })
  .catch(error => console.log(error));
