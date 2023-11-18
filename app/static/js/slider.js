var min_slider = document.getElementById("recordMin");
var min_output = document.getElementById("min_value");

min_slider.oninput = function() {
    min_output.innerHTML = this.value;
}