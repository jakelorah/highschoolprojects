/*
   New Perspectives on JavaScript, 2nd Edition
   Tutorial 2
   Case Problem 2

   Author: Jake Lorah
   Date:   1/17/17

   Function List:
   randInt(lower, upper)
      Used to generate a random integer in the range (lower, upper)

*/
<!-- This function randInt will choose a random tip from the tips.js file  -->
function randInt(lower, upper) {
   var size = upper-lower+1;
   return Math.floor(lower + size*Math.random());
}
