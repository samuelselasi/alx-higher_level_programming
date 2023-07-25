#!/usr/bin/node

const https = require('https');

const URL = process.argv[2];

function handleResponse (response) {
  let data = '';
  response.on('data', (chunk) => {
    data += chunk;
  });

  response.on('end', () => {
    if (response.statusCode !== 200) {
      console.error('Request failed with status code:', response.statusCode);
      return;
    }

    try {
      const completedTasks = JSON.parse(data);
      const todos = {};

      completedTasks.forEach((task) => {
        if (task.completed) {
          if (!todos[task.userId]) {
            todos[task.userId] = 1;
          } else {
            todos[task.userId]++;
          }
        }
      });

      const length = Object.keys(todos).length;
      if (length === 0) {
        console.log('{}');
      } else {
        console.log('{');
        let task = 0;
        for (const key in todos) {
          if (task === length - 1) {
            console.log(`  '${key}': ${todos[key]}`);
          } else {
            console.log(`  '${key}': ${todos[key]},`);
          }
          task++;
        }
        console.log('}');
      }
    } catch (error) {
      console.error('Error parsing JSON data:', error.message);
    }
  });
}

function handleRequestError (error) {
  console.error('Error occurred while making the request:', error.message);
}

function makeRequest (url) {
  const request = https.get(url, (response) => {
    handleResponse(response);
  });

  request.on('error', handleRequestError);
}

if (!URL) {
  console.error('Please provide a valid URL.');
  process.exit(1);
}

makeRequest(URL);
