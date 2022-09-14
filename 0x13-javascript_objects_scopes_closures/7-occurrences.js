#!/usr/bin/node
/**
 * 
 * @param {*} list 
 * @param {*} searchElement 
 * @returns number of occurences of search item in the list
 */

exports.nbOccurences = function (list, searchElement)
{
    let n = 0;
    for (let i = 0; i < list.length; i++) {
        if (list[i] === searchElement) {
            n++;
        }
        
    }
    return n;
}