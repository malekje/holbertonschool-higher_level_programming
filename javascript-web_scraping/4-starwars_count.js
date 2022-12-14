#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = 18;

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    let movies;
    try {
      movies = JSON.parse(body);
    } catch (parseError) {
      console.error(parseError);
      return;
    }

    if (!Array.isArray(movies)) {
      console.error('Expected response body to be an array of movies');
      return;
    }

    const wedgeAntillesMovies = movies.filter(movie => movie.characters.includes(`https://swapi-api.hbtn.io/api/people/${characterId}/`));
    console.log(wedgeAntillesMovies.length);
  }
});
