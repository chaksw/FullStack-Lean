"use strict";

const modal = document.querySelector(".modal");
const overlay = document.querySelector(".overlay");
const btnCloseModal = document.querySelector(".close-modal");
const btnShowModal = document.querySelectorAll(".show-modal");

const openModal = function () {
    // modal.classList.remove("hidden");
    // overlay.classList.remove("hidden");
    modal.style.display = "block";
    overlay.style.display = "block";
};
for (let i = 0; i < btnShowModal.length; i++) {
    btnShowModal[i].addEventListener("click", openModal);
}

const closeModal = function () {
    // modal.classList.add("hidden");
    // overlay.classList.add("hidden");
    modal.style.display = "none";
    overlay.style.display = "none";
};

btnCloseModal.addEventListener("click", closeModal);
overlay.addEventListener("click", closeModal);
document.addEventListener("keyup", function (e) {
    // parament 'e' defined here represented a keyboard event object
    // the keyboard event object will generated once any keyup manipulation
    if (
        e.key == "Escape" &&
        modal.style.display === "block" &&
        overlay.style.display === "block"
    ) {
        closeModal();
    }
    // if (
    //     e.key == "Escape" &&
    //     !modal.classList.contains === "hidden" &&
    //     !overlay.classList.contains === "hidden"
    // ) {
    //     closeModal();
    // }
    // console.log(e.key);
});
