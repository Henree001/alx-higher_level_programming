#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(process.argv[3], body, (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
