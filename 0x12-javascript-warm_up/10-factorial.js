#!/usr/bin/node
/**
 *  a script that computes and prints a factorial
 * The first argument is integer used for computing the factorial
 * Factorial of NaN is 1
 * 
 */

const arg = parseInt(process.argv[2]);


function factorial(num){
    if ((Number.isNaN(num) )|| (num === 1) ) {
        return 1;
    }
    return factorial(num -  1) * num;
    
}
console.log(factorial(arg));