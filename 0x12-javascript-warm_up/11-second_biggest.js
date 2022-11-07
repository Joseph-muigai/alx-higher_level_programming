#!/usr/bin/node
/**
 *  a script that searches the second biggest integer in the list of arguments.
 * 
 */
const myargs = process.argv;

if (myargs.length <= 3)
{
    console.log(0);
}else{
    console.log(myargs.sort((x, y)=> y - x).slice(3)[0]);
}