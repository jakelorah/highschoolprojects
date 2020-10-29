function circumferencecircle(i)
 {
  if(isNaN(i))
    {
     alert("Must be numeric!!");
    }
   else
    {
     var sum = 0;
     sum = (2 * 3.14 * (i));
     document.write("The circumference of a circle is = " + sum);
    }
  }