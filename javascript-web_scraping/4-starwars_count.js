#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = 18;

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const movies = JSON.parse(body);
    const wedgeMovies = movies.filter(movie => {
      return movie.characters.includes(`https://swapi-api.hbtn.io/api/people/${characterId}/`);
    });
    console.log(wedgeMovies.length);
  }
});
