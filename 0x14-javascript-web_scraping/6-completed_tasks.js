#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const obj = {};
    body = JSON.parse(body);
    for (let i = 0; i < body.length; ++i) {
      if (body[i].completed && !obj[body[i].userId]) {
        obj[body[i].userId] = 0;
      }
      if (body[i].completed) {
        obj[body[i].userId]++;
      }
    }
    console.log(obj);
  }
});
