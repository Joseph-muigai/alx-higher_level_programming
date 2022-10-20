#!/usr/bin/node
/**
 * a script that reads and prints the content of a file.
 * first argumrnt is the file path
 * content of the file must be read in utf-8
 * if an error occurs diuring the reading of the file print the error
 */

const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', function (err, data){
    console.log(err || data);
});
