#!/usr/bin/node
/*
Write a script that prints My number: <first argument converted in integer>
 if the first argument can be converted to an integer
*/
const arg = parseInt(process.argv[2]);

if (Number.isNaN(arg))
{
    console.log('Not a number');
}
else
{
 console.log('My number: '+ arg);
}