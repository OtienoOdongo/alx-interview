#!/usr/bin/node

const request = require('request'); // Importing the request library

// Defining the base URL for the Star Wars API
const baseURL = 'https://swapi.dev/api/';

// Function to get character names for a given movie ID
function getMovieCharacters (movieId) {
  // Construct the URL for the movie
  const movieURL = `${baseURL}films/${movieId}/`;

  // Making an API request to get the movie data
  request(movieURL, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const characters = movieData.characters;

      // Iterating through character URLs and printing their names
      characters.forEach((characterURL) => {
        request(characterURL, (charError, charResponse, charBody) => {
          if (!charError && charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          } else {
            console.log(error);
          }
        });
      });
    } else {
      console.log(error);
    }
  });
}

// Get the movie ID from command-line arguments or user input
const movieId = process.argv[2];

if (!movieId) {
  console.log('Error: Movie ID is missing');
} else {
  getMovieCharacters(movieId);
}
