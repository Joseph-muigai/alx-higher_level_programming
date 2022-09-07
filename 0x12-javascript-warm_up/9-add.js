#!/usr/bin/node
/**
 * a script that prints the addition of 2 integers
 * The first argument is the first integer
 * The second argument is the second integer
 * ou have to define a function with this prototype: function add(a, b)
 */

const firstArg  = parseInt(process.argv[2]);
const secondArg  = parseInt(process.argv[3]);

function add(a, b)
{
    total = a + b;
    console.log(total);
}
add(firstArg, secondArg)