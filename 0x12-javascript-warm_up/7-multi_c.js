#!/usr/bin/node
/**
 * Write a script that prints x times “C is fun”
 * Where x is the first argument of the script
 * 
 */

const arg = parseInt(process.argv[2]);
if (Number.isNaN(arg)){
    console.log('Missing number of occurrences');
}else{
    for (let i = 0; i < arg; i++)
    {
        console.log('C is fun');
    }
}
