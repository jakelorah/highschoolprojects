/*
   New Perspectives on JavaScript, 2nd Edition
   Tutorial 2
   Case Problem 3

   Author: Jake Lorah
   Date:   1/19/17

   Function List:
   addTime(oldTime, milliSeconds)
      Used to add a specified number of milliseconds to a date object named oldTime.
      A new date object with the new time value is returned by the function.

   showTime(time)
      Displays a time value in the format:
      hh:mm AM/PM
*/
<!-- This function counts each of the time zones by milliseconds -->
function addTime(oldTime, milliSeconds) {
   var newTime = new Date();
   var newValue = oldTime.getTime()+milliSeconds;
   newTime.setTime(newValue);
   return newTime;
}  
<!-- This function shows only the hour and minutes in the boxes -->
function showTime(time) {
   minute = time.getMinutes();
   hour = time.getHours();
<!-- This is the correct format for the times. Hour, colon, minutes, am/pm  -->
   ampm = (hour < 12) ? "AM" : "PM";
   hour = (hour > 12) ? hour - 12 : hour;
   hour = (hour == 0) ? 12 : hour;
<!-- If minutes is less than 10, then the value of minutes is 0 -->
   minute = minute < 10 ? "0"+minute : minute;
<!-- This returns just the hour, minutes, and either am or pm in each box -->
   return hour+":"+minute+ampm;
}




