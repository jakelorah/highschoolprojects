function pythagoreantheorem(i, ii)
 {
  if(isNaN(i) || isNaN(ii))
    {
     alert("Must be numeric!!");
    }
   else
    {
     var c = 0;
     c = Math.sqrt((i * i) + (ii * ii));
     document.write("The solution for the Pythagorean Theorem is = " + c);
    }
  }