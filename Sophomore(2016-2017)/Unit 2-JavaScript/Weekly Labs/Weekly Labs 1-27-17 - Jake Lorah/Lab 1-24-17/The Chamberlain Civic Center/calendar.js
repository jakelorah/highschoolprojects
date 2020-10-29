/*
   New Perspectives on JavaScript, 2nd Edition
   Tutorial 3
   Tutorial Case

   Author: Jake Lorah 
   Date: 1/24/17   

   Function List:
   calendar(calendarDay)
      Creates the calendar table for the month specified in the
      calendarDay parameter. The current date is highlighted in 
      the table.

   writeCalTitle(calendarDay)
      Writes the title row in the calendar table

   writeDayTitle()
      Writes the weekday title rows in the calendar table

   daysInMonth(calendarDay)
      Returns the number of days in the month from calendarDay

   writeCalDays(calendarDay)
      Writes the daily rows in the calendar table, highlighting
      calendarDay

*/

function calendar() {
    var calDate = new Date("March 18, 2011");

   document.write("<table id='calendar_table'>");
   writeCalTitle(calDate);
   document.write("</table>");
}

function writeCalTitle (calendarDay) {
   var monthName = new Array ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December");

 var thisMonth=calendarDay.getMonth();
 var thisYear=calendarDay.getFullYear();

 document.write("<tr>");
 document.write("<th id='calendar_head' colspan='7'>");
 document.write(monthName[thisMonth]+" "+thisYear);
 document.write("</th>");
 document.write("</tr>");
}
