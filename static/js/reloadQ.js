function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById("forumQ_form").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "forum.html", true);
  xhttp.send();
}