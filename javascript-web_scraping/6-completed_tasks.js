#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');

request.get(args[0], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const users = JSON.parse(body);
    const countTask = countTaskFunction(users);
    console.log(countTask);
  }
});

function countTaskFunction (users) {
  // Obj to store the count of task completed for each user
  const countTask = {};
  let user;
  for (user of users) {
    if (user.completed === true) {
      /* if user already have a record in the object,
        increment by one the count, else set to one. */
      if (countTask[user.userId]) countTask[user.userId] += 1;
      else countTask[user.userId] = 1;
    }
  }
  return countTask;
}
