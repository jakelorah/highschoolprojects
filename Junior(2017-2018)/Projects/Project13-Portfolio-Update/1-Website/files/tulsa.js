/*
   New Perspectives on JavaScript, 2nd Edition
   Tutorial 2
   Review Assignment

   Author: Jake Lorah
   Date:   1/11/17

   Function List:
   showDateTime(time)
      Returns the date in a text string formatted as:
      mm/dd/yyyy at hh:mm:ss am

   changeYear(today, holiday)
      Changes the year value of the holiday object to point to the
      next year if it has already occurred in the present year

   countdown(stop, start)
      Displays the time between the stop and start date objects in the
      text format:
      dd days, hh hrs, mm mins, ss secs
*/
<!-- Making a new function called showDateTime, that will produce the date, month, year  -->
function showDateTime(time) {
   date = time.getDate();
   month = time.getMonth()+1;
   year = time.getFullYear();

   second = time.getSeconds();
   minute = time.getMinutes();
   hour = time.getHours();

   ampm = (hour < 12) ? " a.m." : " p.m.";
   hour = (hour > 12) ? hour - 12 : hour;
   hour = (hour == 0) ? 12 : hour;

   minute = minute < 10 ? "0"+minute : minute;
   second = second < 10 ? "0"+second : second;

   return month+"/"+date +"/"+year+" at "+hour+":"+minute+":"+second+ampm;
}
<!-- Making a new function called changeYear, that will change the year from 2 digits to 4 digits  -->
function changeYear(today, holiday) {
   year=today.getFullYear();
   holiday.setFullYear(year);
   year = (holiday < today) ? year+1 : year;
   holiday.setFullYear(year);
}
<!-- Making a new function callled countdown, that will constantly keep counting down until a certian date. Also I made the format of the countdown days, hrs, mins, secs in that order -->
function countdown(stop, start) {
   time = start-stop;
   days = time/(1000*60*60*24);
   hours = (days - Math.floor(days))*24;
   minutes = (hours - Math.floor(hours))*60;
   seconds = (minutes - Math.floor(minutes))*60;
   return parseInt(days)+" days, "+parseInt(hours)+" hrs, "+parseInt(minutes)+" mins, "+parseInt(seconds)+" secs";
}