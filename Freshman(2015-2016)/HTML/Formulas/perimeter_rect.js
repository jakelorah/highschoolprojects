function add1(i,ii)
 {
  if(isNaN(i) || isNaN(ii))
    {
     alert("Must be numeric!!");
    }
   else
    {
     var sum = 0;
     sum = (parseFloat(i * 2) + parseFloat(ii * 2));
     document.write("The permimeter of a rectangle is="+sum);
    }
  }