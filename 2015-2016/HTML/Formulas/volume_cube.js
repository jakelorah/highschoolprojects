function add1(i,ii,iii)
 {
  if(isNaN(i) || isNaN(ii) || isNaN(iii))
    {
     alert("Must be numeric!!");
    }
   else
    {
     var sum = 0;
     sum = (parseFloat(i) * parseFloat(ii) * parseFloat(iii));
     document.write("The volume of a cube is="+sum);
    }
  }