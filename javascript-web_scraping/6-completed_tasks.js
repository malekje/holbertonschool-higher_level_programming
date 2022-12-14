#!/usr/bin/node
const request = require('request');
const url = process.argv[2] || 'https://jsonplaceholder.typicode.com/todos';

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const tasks = JSON.parse(body);
  const completedTasksByUser = new Map();
  tasks.forEach((task) => {
    if (task.completed) {
      const userId = task.userId;
      if (!completedTasksByUser.has(userId)) {
        completedTasksByUser.set(userId, 0);
      }
      completedTasksByUser.set(userId, completedTasksByUser.get(userId) + 1);
    }
  });
  completedTasksByUser.forEach((count, userId) => {
    console.log(`${userId}${count}`);
  });
});
