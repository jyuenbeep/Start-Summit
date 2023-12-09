function myFunction() {
    /* Get the text field */
    var copyText = document.getElementById("copyText");

    /* Create a temporary textarea to copy the text */
    var tempTextarea = document.createElement("textarea");
    tempTextarea.value = copyText.innerText;
    document.body.appendChild(tempTextarea);

    /* Select the text inside the temporary textarea */
    tempTextarea.select();
    tempTextarea.setSelectionRange(0, 99999); /* For mobile devices */

    /* Copy the text inside the temporary textarea to the clipboard */
    document.execCommand("copy");
    document.body.removeChild(tempTextarea);
  }

  document.addEventListener("DOMContentLoaded", function(event) { 
    var scrollpos = localStorage.getItem('scrollpos');
    if (scrollpos) window.scrollTo(0, scrollpos);
});

window.onbeforeunload = function(e) {
    localStorage.setItem('scrollpos', window.scrollY);
};