"use strict";

// DOM usage
// Use document.querySelector to fetch element define in html with (class, ID, element tag)
// Use textContent to fetch content inside the selected element
/* console.log(document.querySelector('.message').textContent);

let msg = document.querySelector('.message').textContent;
document.querySelector('.message').textContent = '🎉 Correct Number!';
console.log(document.querySelector('.message').textContent);
document.querySelector('.number').textContent = 13;
document.querySelector('.score').textContent = 10;
document.querySelector('.guess').value = 23;
console.log(document.querySelector('.guess').value); */

// Handling Click Event
let secretNumber = Math.trunc(Math.random() * 20) + 1;
let score = 20;
let highscore = 0;

// const displayMessage = function () {
//     document.querySelector(".message").textContent = message;
// }

// function displayMessage() {
//     document.querySelector(".message").textContent = message;
// }

const displayMessage = (message) => {
    document.querySelector(".message").textContent = message;
};

const disableCheck = function () {
    document.getElementsByClassName(".check").disabled = true;
    document.querySelector(".check").style.color = "#eee";
    if (score >= 1) {
        document.querySelector(".check").style.backgroundColor = "#60b347";
        document.querySelector(".check").textContent = "🏆 Congrate!";
    } else {
        document.querySelector(".check").style.backgroundColor = "#222";
        document.querySelector(".check").textContent = "😢 You're A LOSER";
    }
};

// document.querySelector('.number').textContent = secretNumber;
document.querySelector(".check").addEventListener("click", function () {
    const guess = Number(document.querySelector(".guess").value);
    // When there is no input
    if (guess > 20 || guess < 1) {
        document.querySelector(".message").textContent =
            "😑 Wrong Number! must select between 1 and 20";
        return;
    }
    if (!guess) {
        displayMessage("⛔️ No Number!");
        // When player win
    } else if (guess === secretNumber) {
        displayMessage("🎉 Correct Number!");
        if (score > highscore) {
            highscore = score;
            document.querySelector(".highscore").textContent = highscore;
        }
        document.querySelector("body").style.backgroundColor = "#60b347";
        document.querySelector(".number").style.width = "30rem";
        document.querySelector(".number").textContent = secretNumber;
        disableCheck();
        return;
    } else {
        // when guess is too high or too low
        displayMessage(guess > secretNumber ? "📈 Too High!" : "📉 Too Low!");
        // When guess is too low
        score--;
        document.querySelector(".score").textContent = score;
        if (score < 1) {
            displayMessage("⛔️ You lost the game!");
            disableCheck();
        }
    }
});

document.querySelector(".again").addEventListener("click", function () {
    // restore values
    score = 20;
    secretNumber = Math.trunc(Math.random() * 20) + 1;
    displayMessage("Start guessing...");
    document.querySelector(".guess").textContent = "";
    document.querySelector(".score").textContent = score;
    document.querySelector(".number").textContent = "?";
    document.querySelector(".check").textContent = "Check!";
    // reset style
    document.querySelector("body").style.backgroundColor = "#222";
    document.querySelector(".number").style.width = "15rem";
    document.getElementsByClassName(".check").disabled = false;
    document.querySelector(".check").style.backgroundColor = "#eee";
    document.querySelector(".check").style.color = "#222";
});
