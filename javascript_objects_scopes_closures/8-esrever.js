#!/usr/bin/node
exports.esrever = function (list) {
  const leng = Math.floor(list.length / 2);
  for (let i = 0; i < leng; i++) {
    list[i] = [
      list[list.length - (i + 1)],
      (list[list.length - (i + 1)] = list[i])
    ][0];
  }
  console.log(list);
};
