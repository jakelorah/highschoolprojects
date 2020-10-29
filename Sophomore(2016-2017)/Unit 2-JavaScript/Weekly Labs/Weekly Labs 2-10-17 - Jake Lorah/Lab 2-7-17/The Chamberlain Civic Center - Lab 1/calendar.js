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

function calendar(calendarDay) {
   if (calendarDay == null) calDate=new Date()
   else calDate = new Date(calendarDay);

   document.write("<table id='calendar_table'>");
   writeCalTitle(calDate);
   writeDayNames();
   writeCalDays(calDate);
   document.write("</table>");
}

function writeCalTitle(calendarDay) {
   var monthName = new Array("January", "February", "March",
  "April", "May", "June", "July", "August", "September",
  "October", "November", "December");
	
   var thisMonth=calendarDay.getMonth();
   var thisYear=calendarDay.getFullYear();

   document.write("<tr>");
   document.write("<th id='calendar_head' colspan='7'>");
   document.write(monthName[thisMonth]+" "+thisYear);
   document.write("</th>");
   document.write("</tr>");
}

function writeDayNames() {
   var dayName = new Array("Sun", "Mon", "Tue", "Wed", "Thu", 
                           "Fri", "Sat");
   document.write("<tr>");
   for (var i=0;i < dayName.length;i++) {
      document.write("<th class='calendar_weekdays'> "+dayName[i]+"</th>");
   }
   document.write("</tr>");
}

function daysInMonth(calendarDay) {
   var thisYear = calendarDay.getFullYear();
   var thisMonth = calendarDay.getMonth();
   var dayCount = new Array(31,28,31,30,31,30,31,31,30,31,30,31);

   if (thisYear % 4 == 0) {
      if ((thisYear % 100 != 0) || (thisYear % 400 == 0)) {
         dayCount[1] = 29; // this is a leap year
      }
   }

   return dayCount[thisMonth]; // return the number of days in the month
}

function writeCalDays(calendarDay) {
   var currentDay = calendarDay.getDate();

   // determine the starting day of the week
   var dayCount = 1;
   var totalDays = daysInMonth(calendarDay);
   calendarDay.setDate(1);              // set the date to the first day of the month
   var weekDay = calendarDay.getDay();  // the day of week of the first day

   // write blank cells preceding the starting day
   document.write("<tr>");
   for (var i=0; i < weekDay; i++) {
      document.write("<td></td>");
   }

   // write cells for each day of the month
   while (dayCount <= totalDays) {
      // write the table rows and cells
      if (weekDay == 0) document.write("<tr>");

      if (dayCount == currentDay) {
         // highlight the current day
         document.write("<td class='calendar_dates' id='calendar_today'>"+dayCount+"</td>");
      } else {
         // display the day as usual
         document.write("<td class='calendar_dates'>"+dayCount+"</td>");
      }

      if (weekDay == 6) document.write("</tr>");

      // move to the next day
      dayCount++;
      calendarDay.setDate(dayCount);
      weekDay = calendarDay.getDay();

   }

   document.write("</tr>");
}