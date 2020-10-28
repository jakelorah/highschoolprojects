/*
   New Perspectives on JavaScript, 2nd Edition
   Tutorial 2
   Tutorial Case

   Author: Jake Lorah 
   Date: 12/21/16   

   Function List:
   showDate(dateObj)
      Returns the current date in the format mm/dd/yyyy

   showTime(dateObj)
      Returns the current time in the format hh:mm:ss am/pm

   calcDays(currentDate)
      Returns the number of days between the current date and January 1st
      of the next year

*/
    function showDate (dateObj) {
      thisDate = dateObj.getDate();
      thisMonth = dateObj.getMonth()+1;
      thisYear = dateObj.getFullYear();
      return thisMonth + "/" + thisDate + "/" + thisYear;
   }

    function showTime (dateObj) {
      thisSecond = dateObj.getSeconds();
      thisMinute = dateObj.getMinutes();
      thisHour = dateObj.getHours();
      return thisHour + ":" + thisMinute + ":" + thisSecond;
   }

  


