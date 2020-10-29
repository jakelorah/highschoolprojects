function areacircle(i)
 {
  if(isNaN(i))
    {
     alert("Must be numeric!!");
    }
   else
    {
     var sum = 0;
     sum = (3.14 * (i * i));
     document.write("The area of a circle is = " + sum);
    }
  }