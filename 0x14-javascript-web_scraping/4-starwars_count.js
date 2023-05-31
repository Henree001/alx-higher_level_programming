#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    body = JSON.parse(body).results;
    for (const item of body) {
      for (const characters of item.characters) {
        if (characters.split('/')[5] === '18') {
          count++;
        }
      }
    }
    console.log(count);
  }
});
