#!/usr/bin/node
/**
 * a function that returns the reversed version of a list
 * Prototype: exports.esrever = function (list)
 * 
 */
exports.esrever = function (list)
{
    let reversedArray = [];
    for (let i = 0; i < list.length; i++) {
        reversedArray.unshift(list[i]);        
    }
    return reversedArray;
}