#!/usr/bin/node

// Importing the 'request' library
const request = require('request');

// Defining the base URL for Stawars api
const apiUrl = 'https://swapi-api.hbtn.io/api/';

// Function to retrieve character names for a given movie ID
function fetchCharacters (characters) {
  // Check if there are more characters to process
  if (characters.length > 0) {
    // Make a GET request to fetch character data
    request.get({ url: characters.shift() }, function (err, res, body) {
      if (!err) {
        // Parse the character data and print the character name
        console.log(JSON.parse(body).name);
        // Recursively call the function to process the next character
        fetchCharacters(characters);
      } else {
        // Handle any errors in the request
        console.log(err);
      }
    });
  }
}

// Retrieve the movie ID from command-line arguments
const movie = process.argv[2];

// Construct the URL for the movie data
const url = apiUrl + 'films/' + movie + '/';

// Make a GET request to fetch movie data
request.get({ url }, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    // Parse the movie data and get the list of characters
    const characters = JSON.parse(body).characters;
    // Call the function to fetch and display character names
    fetchCharacters(characters);
  } else {
    // Handle any errors in the request
    console.log(error);
  }
});
