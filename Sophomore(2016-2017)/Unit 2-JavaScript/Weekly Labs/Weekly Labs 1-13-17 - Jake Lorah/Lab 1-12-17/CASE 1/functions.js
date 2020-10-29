/*
   New Perspectives on JavaScript, 2nd Edition
   Tutorial 2
   Case Problem 1

   Function List:
   showQuiz()
      Used to make the quiz questions visible

   hideQuiz()
      Used to hide the quiz questions
*/

<!-- Create a new function called showQuiz -->
function showQuiz() {
   document.getElementById("quiztable").style.visibility="visible";
}
<!-- Create a new function called hideQuiz -->
function hideQuiz() {
   document.getElementById("quiztable").style.visibility="hidden";
}
<!-- Create a new function called gradeQuiz, that will mark if you get a question write or not -->
function gradeQuiz() {
   correct=0;
   if (document.quiz.q1[2].checked) correct++;
   if (document.quiz.q2[0].checked) correct++;
   if (document.quiz.q3[3].checked) correct++;
   if (document.quiz.q4[0].checked) correct++;
   if (document.quiz.q5[3].checked) correct++;
   <!-- This is the yellow that shows up behind the right answer -->
   document.getElementById("cor1").style.backgroundColor="yellow";
   document.getElementById("cor2").style.backgroundColor="yellow";
   document.getElementById("cor3").style.backgroundColor="yellow";
   document.getElementById("cor4").style.backgroundColor="yellow";
   document.getElementById("cor5").style.backgroundColor="yellow";
   for (i=0; i<document.quiz.elements.length; i++) document.quiz.elements[i].disabled=true;
   return correct;
}