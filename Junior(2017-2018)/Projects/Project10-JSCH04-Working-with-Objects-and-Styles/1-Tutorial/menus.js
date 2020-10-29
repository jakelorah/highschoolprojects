/*
   New Perspectives on JavaScript, 2nd Edition
   Tutorial 4
   Tutorial Case

   Author: Jake Lorah    
   Date: 2/12/18      

   Filename:  menus.js

   -------------------------------------------------------------
   Function List:
   init()
      Initializes the contents of the holmes.htm Web page, setting
      the display property of the pull-down menus and the initial
      values of the global variables

   moveMenu()
      Moves the active menu from one pull-down menu to another

   changeMenu()
      Change the active menu displayed in the document

   closeOldMenu()
      Closes the active menu

   rollDown()
      Applies a roll-down effect the opening of the active menu 

   -------------------------------------------------------------
   Global Variable List:

   activeMenu
      An object variable pointing to the currently active and open menu
   
   timeID
      A variable containing the id of a timed command using the setInterval method

   clipHgt
      The current height of the active menu as it is being rolled down

   -------------------------------------------------------------
*/

window.onload = init;

var activeMenu = null;
var clipHgt = 0;
var timeID;

function init() {
   var menus = new Array();
   var allElems = document.getElementsByTagName("*");

   for (var i = 0; i < allElems.length; i++) {
      if (allElems[i].className == "menu") menus.push(allElems[i]);
   }

   for (var i = 0; i < menus.length; i++) {
      menus[i].onclick = changeMenu;
      menus[i].onmouseover = moveMenu;
   }

   document.getElementById("logo").onclick = closeOldMenu;
   document.getElementById("linkList").onclick = closeOldMenu;
   document.getElementById("main").onclick = closeOldMenu;
}

function moveMenu() {
    // this function moves the pull-down menu from one title to another

    if (activeMenu) {
        closeOldMenu();

        menuID = this.id + "List";
        activeMenu = document.getElementById(menuID);
        activeMenu.style.clip = "rect(0px, 150px, 0px, 0px)";
        activeMenu.style.display = "block";
        timeID = setInterval("rollDown()", 1);
     }
}

function changeMenu() {
   // this function changes the pull-down menu displayed in the document

   closeOldMenu();

   menuID = this.id + "List";
   activeMenu = document.getElementById(menuID);
   activeMenu.style.clip = "rect(0px, 150px, 0px, 0px)";
   activeMenu.style.display = "block";
   timeID = setInterval("rollDown()", 1);
}


function closeOldMenu() {
    if (activeMenu) {
        clearInterval(timeID);
        activeMenu.style.display = "none";
        activeMenu = null;
     }
}


function rollDown() {
    clipHgt = clipHgt + 10;
    if (clipHgt < 400) {
        activeMenu.style.clip = "rect(0px, 150px," + clipHgt + "px, 0px)";
     } else {
         clearInterval(timeID);
         clipHgt = 0;
     }
}

