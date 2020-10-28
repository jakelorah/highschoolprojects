function add1(i,ii)
 {
  if(isNaN(i) || isNaN(ii))
    {
     alert("Must be numeric!!");
    }
   else
    {
     var sum = 0;
     sum = (parseFloat(i) * parseFloat(ii));
     document.write("The area of a rectangle is="+sum);
    }
  }