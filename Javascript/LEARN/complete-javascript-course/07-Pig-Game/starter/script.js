"use strict";

// Variabls
// in using querySelector, we refer id/class in a same way as in css
// in using getElementById, we refer directly the name of id
const player0El = document.querySelector(".player--0");
const player1El = document.querySelector(".player--1");

const score0El = document.querySelector("#score--0");
const current0El = document.getElementById("current--0");
const current1El = document.getElementById("current--1");
// get element by ID
const score1El = document.getElementById("score--1");
const diceEl = document.querySelector(".dice");

const btnNew = document.querySelector(".btn--new");
const btnRoll = document.querySelector(".btn--roll");
const btnHold = document.querySelector(".btn--hold");

let playing, currentScore, activePlayer, scores;

const init = function () {
	playing = true;
	currentScore = 0;
	activePlayer = 0;
	scores = [0, 0];

	score0El.textContent = 0;
	current0El.textContent = 0;
	score1El.textContent = 0;
	current1El.textContent = 0;

	diceEl.classList.add("hidden");
	player0El.classList.remove("player--winner");
	player1El.classList.remove("player--winner");
	player1El.classList.remove("player--active");
	player0El.classList.add("player--active");
};

// Update score to crruent play and swtich player
const switchPlayer = function () {
	// reset current score to total score
	currentScore = 0;
	document.getElementById(`current--${activePlayer}`).textContent = 0;
	activePlayer = activePlayer === 0 ? 1 : 0;
	// toggle statue (add/remove) player
	player0El.classList.toggle("player--active");
	player1El.classList.toggle("player--active");
	// if (player0El.classList.contains("player--active")) {
	// 	player0El.classList.remove("player--active");
	// 	player1El.classList.add("player--active");
	// } else {
	// 	player1El.classList.remove("player--active");
	// 	player0El.classList.add("player--active");
	// }
};

const holdGame = function () {
	if (playing) {
		// 1. add current score to active player's score
		scores[activePlayer] += currentScore;
		document.querySelector(`#score--${activePlayer}`).textContent =
			scores[activePlayer];
		// Swtich next player
		if (scores[activePlayer] >= 20) {
			playing = false;
			diceEl.classList.add("hidden");
			document.querySelector(
				`#name--${activePlayer}`
			).textContent = `Player ${activePlayer + 1} Win ! 🎉🎉🎉🎉🎉`;
			alert(`Player ${activePlayer + 1} wins ! 🎉🎉🎉🎉🎉`);

			document
				.querySelector(`.player--${activePlayer}`)
				.classList.add("player--winner");

			document
				.querySelector(`.player--${activePlayer}`)
				.classList.remove("player--active");
		} else {
			switchPlayer();
		}
	}
};

const rollDice = function () {
	if (playing) {
		// 1. get a random number
		let dice = Math.trunc(Math.random() * 6) + 1;

		// 2. display roll as per number
		// * attribute 'src' of element can be called in this way
		diceEl.src = `dice-${dice}.png`;
		diceEl.classList.remove("hidden");

		// 3. check for rolled 1: if true, swtich player
		if (dice === 1) {
			switchPlayer();
		} else {
			// Add dice number to current score
			currentScore += dice;
			document.getElementById(`current--${activePlayer}`).textContent =
				currentScore;
		}
	}
};

init();

btnRoll.addEventListener("click", rollDice);
btnHold.addEventListener("click", holdGame);
btnNew.addEventListener("click", init);
