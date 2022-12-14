#!/usr/bin/node

const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api/films/';
const CHARACTER_ID = 18;

request.get(API_URL, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body);

  const movies = data.results.filter(movie => movie.characters.includes(`https://swapi-api.hbtn.io/api/people/${CHARACTER_ID}/`));
  console.log(`${movies.length}`);
});
