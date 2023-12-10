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
    "I use a password manager to create and store my passwords (ex. BitLocker, BitWarden, etc.)", //1 yes
    "I use the same password over and over again", //2 no
    "I turn on multifactor authentication (2FA) when given the option", //3 yes
    "I use a VPN when roaming the internet", //4 yes
    "I always update my software to keep it up to date", //5 yes
    "I prioritize using websites with the scheme https instead of http", //6 yes
    "I always click \"Accept All Cookies\" on a website when prompted", //7 no
    "I always check the link address before clicking on them", //8 yes
]

const correctBank = ["a1", "a2", "a1", "a1", "a1", "a1", "a2", "a1"]
const wrongBank = ["a2", "a1", "a2", "a2", "a2", "a2", "a1", "a2"]

const topicBank = [
    "Using password manager", //1
    "Creating a strengthened password", //2
    "Using 2FA(multi-factor authentication)", //3
    "Using a VPN", //4
    "Implementing applications or software", //5
    "Internet Protocol", //6
    "Dangers of accepting cookies", //7
    "Phishing", //8
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
    "[info for 2FA]",
    // 4
    "Enhance cybersecurity by installing trusted software like antivirus protection softwarres like NordVPN to protect against scammers.",
    // 5
    "Enhance cybersecurity by installing trusted software like antivirus protection softwarres like NordVPN to protect against scammers.",
    // 6
    "Check your internet protocol for better cybersecurity; the \"s\" in the link indicates encryption, preventing hackers from stealing cookies and personal data. Use \"HTTPS\" for secure information sharing.",
    // 7
    "Cookies are small amounts of data that are used to identify your computer and personal info to make the user experience more personalized. The data in cookies are usually harmless but may jeapordise your privacy if they fall into the wrong hands.",
    // 8
    "With phising being the #1 crime type globally, it's important to read your links carefully!",
]

answerClicked = [false, false, false, false, false, false, false, false]

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
        // document.getElementById("q"+qNum).style.backgroundColor = "lightblue"
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