/*
   New Perspectives on JavaScript, 2nd Edition
   Tutorial 2
   Case Problem 4

   Author: Jake Lorah 
   Date: 1/19/17   

   Function List:
   dayDiff(start, stop)
      Calculates the number of days, rounded down the next lowest integer, 
      between a starting date and stopping date.

   hoursDiff(start, top)
      Calculates the number of hours left in the current day rounded down 
      to the next lowest integer between a starting date and the stopping date.

   minutesDiff(start, stop)
      Calculates the number of minutes left in the current hour rounded down 
      to the next lowest integer between a starting date and the stopping date.

   showDate(time)
      Displays the value of the time object in the format:
      mm/dd/yyyy

   showTime(time)
      Displays the value of the time object in the format:
      hh:mm am/pm
*/

<!-- This function calculates the starting date and the stopping date  -->
function daysDiff(start, stop) {
       return Math.floor((stop - start)/(1000*60*60*24));
}
<!-- This function calculates the hours left in the current day between start and stop dates  -->
function hoursDiff(start, stop) {
      var daysLeft = (stop-start)/(1000*60*60*24);
      return Math.floor((daysLeft - daysDiff(start, stop))*24);
}
<!-- This function calculates the minutes left in the current hour between start and stop dates  -->
function minutesDiff(start, stop) {
       var daysLeft = (stop-start)/(1000*60*60*24);
      var hoursLeft = (daysLeft - daysDiff(start, stop))*24;
      return Math.floor((hoursLeft - hoursDiff(start, stop))*60);
}
<!-- This function shows the date in the correct format  -->
function showDate(dateObj) {
   thisDate = dateObj.getDate();
   thisMonth = dateObj.getMonth()+1;
   thisYear = dateObj.getFullYear();
   return thisMonth + "/" + thisDate + "/" + thisYear;
}
<!-- This function shows the time in correct format  -->
function showTime(dateObj) {
  thisSecond=dateObj.getSeconds();
   thisMinute=dateObj.getMinutes();
   thisHour=dateObj.getHours();
<!-- change thisHour from 24-hour time to 12-hour time -->
     var ampm = (thisHour < 12) ? " a.m." : " p.m.";
<!-- subtracts 12 from the thisHour variable -->
  thisHour = (thisHour > 12) ? thisHour - 12 : thisHour;
<!-- if thisHour equals 0, change it to 12 -->
    thisHour = (thisHour == 0) ? 12 : thisHour;
<!-- add leading zeros to minutes and seconds less than 10 -->
   thisMinute = thisMinute < 10 ? "0"+thisMinute : thisMinute;
   thisSecond = thisSecond < 10 ? "0"+thisSecond : thisSecond;
<!-- returns hours, minutes, seconds -->
   return thisHour + ":" + thisMinute + ":" + thisSecond + ampm;
}