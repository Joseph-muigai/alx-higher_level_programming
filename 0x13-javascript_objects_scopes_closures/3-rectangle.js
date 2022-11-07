#!/usr/bin/node
/**
 *  a class Rectangle that defines a rectangle
 * The constructor must take 2 arguments w and h
 * Initialize the instance attribute width with the value of w
 * Initialize the instance attribute height with the value of h
 * If w or h is equal to 0 or not a positive integer, create an empty object
 * 
 */

 class Rectangle{
    constructor(w,h){
        if ( w > 0 && h > 0) {
            
            this.width = w;
            this.height = h;
        }
    }
    print(){
        for (let index = 0; index < this.height; index++) {
            console.log('X'.repeat(this.width));            
        }
    }
}
module.exports = Rectangle