window.onload = init;

function init() {
   var menuTabs = new Array();
   var allSelect = document.getElementsByTagName("select");

   for (var i=0; i< allSelect.length; i++) allSelect[i].onchange=loadLink;

}

function loadLink() {
   sIndex = this.selectedIndex;
   location.href = this.options[sIndex].value;
}