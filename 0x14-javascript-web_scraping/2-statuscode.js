#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (eror, response, body) {
  console.log('code:', response.statusCode); // Print the response status code if a response was received
});
