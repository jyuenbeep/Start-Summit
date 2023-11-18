var rMin_slider = document.getElementById("recordMin");
var rMin_output = document.getElementById("recordMin_value");

rMin_slider.oninput = function() {
    rMin_output.innerHTML = this.value;
}

var yMin_slider = document.getElementById("yearMin");
var yMin_output = document.getElementById("yearMin_value");

yMin_slider.oninput = function() {
    yMin_output.innerHTML = this.value;
}