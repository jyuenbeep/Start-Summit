// Initialize Variables
var closePopup = document.getElementById("popupclose");
var overlay = document.getElementById("overlay");
var popup = document.getElementById("popup");

// Close Popup Event
closePopup.onclick = function() {
  overlay.style.display = 'none';
  popup.style.display = 'none';
};

// Show Overlay and Popup

const questionBank = [
    "Do you use a password manager? (ex. BitLocker)",
    "Do you turn on multifactor authentication (2FA)?",
    "Do you use a VPN when roaming the internet?",
    "Do you keep your software up to date?",
    "Which of the following is more secure?",
    "Do you check links before clicking on them?",
    "Do you use the same password over and over again?"
]

const correctBank = ["a1", "a1", "a1", "a1", "a2", "a1", "a2"]
const wrongBank = ["a2", "a2", "a2", "a2", "a1", "a2", "a1"]

const topicBank = [
    // 1
    "Creating a strengthened password",
    // 2
    "Using password manager & 2FA(multi-factor authentication)",
    // 3
    "Phishing",
    // 4
    "Internet Protocol",
    // 5
    "Implementing applications or software",
    // 6
    "Dangers of accepting cookies",
    // 7
]

const infoBank = [
    // 1
    `Here are some recommendations to improve your password:
    <p> - Make it at least 15 characters</p>
    <p> - Make passwords unique — never used before</p>
    <p> - Randomly generate — utilize a computer or password manaher</p>`,
    // 2
    `Utilizing PIN numbers, authentication application or confirmation 
    text on your phone, or fingerprint or face ID to prevent hackers from being`,
    // 3
    "With phising being the #1 crime type globally, it's important to read your links carefully!",
    // 4
    "Check your internet protocol for better cybersecurity; the \"s\" in the link indicates encryption, preventing hackers from stealing cookies and personal data. Use \"HTTPS\" for secure information sharing.",
    // 5
    "Enhance cybersecurity by installing trusted software like antivirus protection softwarres like NordVPN to protect against scammers.",
    // 6
    "Cookies are small amounts of data that are used to identify your computer and personal info to make the user experience more personalized. The data in cookies are usually harmless but may jeapordise your privacy if they fall into the wrong hands.",
    // 7
]

answerClicked = [false, false, false, false, false, false]

function displayQuestion(qNum) {
    overlay.style.display = 'block';
    popup.style.display = 'block';
    const element = document.getElementById("questionText");
    element.innerHTML = questionBank[qNum];
    
    function changeCard() {
        document.getElementById("topic").innerHTML = topicBank[qNum]
        document.getElementById("info").innerHTML = infoBank[qNum]
    }

    function doneAnswering() {
        answerClicked[qNum] = true
        document.getElementById("q"+qNum).style.backgroundColor = "lightblue"
    }

    document.getElementById(correctBank[qNum]).onclick = function() {
        if (!answerClicked[qNum]) {
            const e = document.getElementById("correctNum")
            const correctNew = (parseInt(e.innerHTML) + 1).toString()
            e.innerHTML = correctNew
            doneAnswering()
        }
        changeCard()
    }
    document.getElementById(wrongBank[qNum]).onclick = function() {
        if (!answerClicked[qNum]) {
            const e = document.getElementById("wrongNum")
            const wrongNew = (parseInt(e.innerHTML) + 1).toString()
            e.innerHTML = wrongNew
            doneAnswering()
        }
        changeCard()
    }
}






