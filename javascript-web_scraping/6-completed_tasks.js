#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');

request.get(args[0], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const users = JSON.parse(body);
    // Obj to store the count of task completed for each user
    const countTask = {};
    /* This array counts in the fist index the id of the user,
     and the second contains the number of task completed */
    const currentCount = [0, 0];
    let user;
    for (user of users) {
      /* If the current count not is the same as the user id reset
       the current count */
      if (currentCount[0] !== user.userId) {
        currentCount[0] = user.userId;
        currentCount[1] = 0;
      }
      if (user.completed) currentCount[1] += 1;
      countTask[user.userId] = currentCount[1];
    }
    console.log(countTask);
  }
});
