#!/usr/bin/node

/**
 * a function that prints the number of arguments already printed and the new argument value
 * Prototype: exports.logMe = function (item)
 * 
 */
let n = 0
exports.logMe = function (item){
    console.log(`${n}: ${item}`);
    n++;
}