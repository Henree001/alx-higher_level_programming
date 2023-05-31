#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    let count = 0;
    const obj = {};
    body = JSON.parse(body);
    for (let i = 0; i < body.length; ++i) {
      if (body[i].completed) {
        count++;
      }
      if (i === 19 || i === 39 || i === 59 || i === 79 || i === 99 ||
                i === 119 || i === 139 || i === 159 || i === 179 || i === 199) {
        obj[body[i].userId] = count;
        count = 0;
      }
    }
    console.log(obj);
  }
});
