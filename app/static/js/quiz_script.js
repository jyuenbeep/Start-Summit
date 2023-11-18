//vars
var correctScore = 0;
var wrongScore = 0;

var questionCount = 0;

//store values
var result = document.getElementById("result");
var q1a1 = document.getElementById("q1a1");
var q1a2 = document.getElementById("q1a2");
var q2a1 = document.getElementById("q2a1");
var q2a2 = document.getElementById("q2a2");
var q3a1 = document.getElementById("q3a1");
var q3a2 = document.getElementById("q3a2");
var q4a1 = document.getElementById("q4a1");
var q4a2 = document.getElementById("q4a2");
var q5a1 = document.getElementById("q5a1");
var q5a2 = document.getElementById("q5a2");
var q6a1 = document.getElementById("q6a1");
var q6a2 = document.getElementById("q6a2");
var q7a1 = document.getElementById("q7a1");
var q7a2 = document.getElementById("q7a2");
var q8a1 = document.getElementById("q8a1");
var q9a2 = document.getElementById("q8a2");

var restart = document.getElementById("restart");

//event listeners
q1a1.addEventListener("click", correct);
q2a2.addEventListener("click", correct);
q3a1.addEventListener("click", correct);
q4a1.addEventListener("click", correct);
q5a1.addEventListener("click", correct);
q6a2.addEventListener("click", correct);
q7a1.addEventListener("click", correct);
q8a2.addEventListener("click", correct);

q1a2.addEventListener("click", wrong);
q2a1.addEventListener("click", wrong);
q3a2.addEventListener("click", wrong);
q4a2.addEventListener("click", wrong);
q5a2.addEventListener("click", wrong);
q6a1.addEventListener("click", wrong);
q7a2.addEventListener("click", wrong);
q8a1.addEventListener("click", wrong);

restart.addEventListener("click", rest);

//disable
q1a1.addEventListener("click", disablebuttons1);
q1a2.addEventListener("click", disablebuttons1);

q2a1.addEventListener("click", disablebuttons2);
q2a2.addEventListener("click", disablebuttons2);

q3a2.addEventListener("click", disablebuttons3);
q3a1.addEventListener("click", disablebuttons3);

q4a2.addEventListener("click", disablebuttons4);
q4a1.addEventListener("click", disablebuttons4);

q5a2.addEventListener("click", disablebuttons5);
q5a1.addEventListener("click", disablebuttons5);

q6a2.addEventListener("click", disablebuttons6);
q6a1.addEventListener("click", disablebuttons6);

q7a2.addEventListener("click", disablebuttons7);
q7a1.addEventListener("click", disablebuttons7);

q8a2.addEventListener("click", disablebuttons8);
q8a1.addEventListener("click", disablebuttons8);

//correct
function correct() {
  correctScore += 1;
  questionCount += 1;

  if (questionCount == 8) {
    updateResult();
  }
}

//wrong
function wrong() {
  wrongScore += 1;
  questionCount += 1;

  if (questionCount == 8) {
    updateResult();
  }
}

//restart
function rest() {
  result.innerHTML = "YOUR RESULT IS...";
  questionCount = 0;
  correctScore = 0;
  wrongScore = 0;
  enablebuttons();
  // console.log("hihih")
  
  btnElList.forEach(btnEl => {
      btnEl.classList.remove('special')
  })
}

  function disablebuttons1() {
    document.getElementById("q1a1").disabled = true;
    document.getElementById("q1a2").disabled = true;
  }

  function disablebuttons2() {
    document.getElementById("q2a1").disabled = true;
    document.getElementById("q2a2").disabled = true;
  }

  function disablebuttons3() {
    document.getElementById("q3a1").disabled = true;
    document.getElementById("q3a2").disabled = true;
  }

  function disablebuttons4() {
    document.getElementById("q4a1").disabled = true;
    document.getElementById("q4a2").disabled = true;
  }
  
  function disablebuttons5() {
    document.getElementById("q5a1").disabled = true;
    document.getElementById("q5a2").disabled = true;
  }

  function disablebuttons6() {
    document.getElementById("q6a1").disabled = true;
    document.getElementById("q6a2").disabled = true;
  }

  function disablebuttons7() {
    document.getElementById("q7a1").disabled = true;
    document.getElementById("q7a2").disabled = true;
  }

  function disablebuttons8() {
    document.getElementById("q8a1").disabled = true;
    document.getElementById("q8a2").disabled = true;
  }

  function enablebuttons() {
    document.getElementById("q1a1").disabled = false;
    document.getElementById("q1a2").disabled = false;

    document.getElementById("q2a1").disabled = false;
    document.getElementById("q2a2").disabled = false;

    document.getElementById("q3a1").disabled = false;
    document.getElementById("q3a2").disabled = false;

    document.getElementById("q4a1").disabled = false;
    document.getElementById("q4a2").disabled = false;
    
    document.getElementById("q5a1").disabled = false;
    document.getElementById("q5a2").disabled = false;

    document.getElementById("q6a1").disabled = false;
    document.getElementById("q6a2").disabled = false;

    document.getElementById("q7a1").disabled = false;
    document.getElementById("q7a2").disabled = false;

    document.getElementById("q8a1").disabled = false;
    document.getElementById("q8a2").disabled = false;
  }

//results
function updateResult() {
  if (correctScore >= 7) {
    result.innerHTML = "Congradulations! You are proficient in basic cybersecurity!!";
  }
  else if (wrongScore > 1) {
    result.innerHTML = ":( You should check our Resources to improve your cybersecurity knowledge";
  }
}

const btnElList = document.querySelectorAll('button');
btnElList.forEach(btnEl => {
  btnEl.addEventListener('click', () => {
    // if (btnEl.getElementById('restart')){
    //   return
    // } else {
    btnEl.classList.add('special')
    // }
  })
})
