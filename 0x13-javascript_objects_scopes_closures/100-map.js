#!/usr/bin/node
/**
 * a script that imports an array and computes a new array.
 * use map
 * A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
 * 
 */
 
const list = require('./100-data.js').list;
console.log(list);

console.log(list.map((item, index) => item * index))