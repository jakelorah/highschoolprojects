/*
   New Perspectives on JavaScript, 2nd Edition
   Tutorial 1
   Review Assignment


   Function List:
   randomInteger()
      Used to reverse the order of characters in a text string

*/


function randomInteger(size) {
   var result=Math.floor((size+1)*Math.random());
   return result;
}