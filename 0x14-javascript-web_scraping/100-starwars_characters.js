#!/usr/bin/node
const request = require('request');
const requesturl = 'https://swapi.co/api/films/' + process.argv[2];
request(requesturl, function (error, response, body){
	if (!error) {
		const characters = JSON.parse(body).characters;
		character.forEach((character) => {
			request(character, function (error, response, body) {
				if (!error) {
					console.log(JSON.parse(body).name);
				}
			});
		})
	}
});
