"use strict"; // use strict mode
// During development, we need to use the uptodate Google Chrome to ensure our code could be used in
// the latest javascript standard
/* 
// After developpment, to ensure our development could be used in any versioin of browser
// we use Babel to transpile and polyfill code (converting back to ES5 to ensure browser compatibility for all users)
let hasDriversLicense = false;
const passTest = true;

if (passTest) hasDriversLicense = true;
if (hasDriversLicense) console.log("I can dirve :D");

// some word (variable name) is reserved, in strict mode, defining them will cause syntaxError
// but without declaration of 'use strict', this kind of error will not show
// const interface = "Audio";
// const private = 534;

// in using function declaration, function could be called before its'definition
// but we could not called the function expresiion before defining it.
// Function
function logger() {
    console.log("My name is Jonas");
}

// calling/running/invoking function
logger();

function fruitProcessor(apples, oranges) {
    console.log(apples, oranges);
    const juice = `Juice with ${apples} apples🍎 and ${oranges} oranges🍊`;
    return juice;
}

const appleJuice = fruitProcessor(5, 0);
console.log(appleJuice);

const appleOrangeJuice = fruitProcessor(2, 4);
console.log(appleOrangeJuice);

// Function declaration
function calcAge1(birthYear) {
    // const age = 2037 - birthYear;
    // return age;
    return 2037 - birthYear;
}

const age1 = calcAge1(1991);
console.log(age1);

// Anonymity function, also called function expression
const calcAge2 = function (birthYear) {
    return 2037 - birthYear;
};

const age2 = calcAge2(1991);
console.log(age1, age2);

// Arrow function, it's a function expression, the return value is implicit
// in this function, birthYear is input parameter, and the returne value is implicit (2037 - birthYear)
const calcAge3 = (birthYear) => 2037 - birthYear;
const age3 = calcAge3(2000);
console.log(age3);

// Arrow function with parameter
// const yearUntilRetirement = (birthYear) => {
//     const age = 2037 - birthYear;
//     const retirement = 65 - age;
//     return retirement;
// };

// console.log(yearUntilRetirement(1991));

// Arrow function with multiple parameter
const yearUntilRetirement = (birthYear, firstName) => {
    const age = 2037 - birthYear;
    const retirement = 65 - age;
    return `${firstName} retires in ${retirement} years`;
};

console.log(yearUntilRetirement(1991, "Jonas"));
console.log(yearUntilRetirement(1980, "Bob")); */

/* // Functions calling other functions
function cutFruitPieces(fruit) {
    return fruit * 4;
}

function fruitProcessor(apples, oranges) {
    const applePieces = cutFruitPieces(apples);
    const orangePieces = cutFruitPieces(oranges);
    const juice = `Juice with ${applePieces} apples🍎 and ${orangePieces} oranges🍊`;
    return juice;
}

console.log(fruitProcessor(2, 3)); */
/* const calcAge = function (birthYear) {
    return 2037 - birthYear;
};

const yearUntilRetirement = function (birthYear, firstName) {
    const age = calcAge(birthYear);
    const retirement = 65 - age;
    if (retirement > 0) {
        return `${firstName} retires in ${retirement} years`;
    } else {
        return `${firstName} has already retired 😀`;
    }
};

console.log(yearUntilRetirement(1991, "Jonas"));
console.log(yearUntilRetirement(1970, "Mike")); */

// Code Challenage 1
/* const calcAverage = (score1, score2, score3) => (score1 + score2 + score3) / 3;
let avgDolphins = calcAverage(44, 23, 71);
let avgKoalas = calcAverage(65, 54, 49);
console.log(avgDolphins, avgKoalas);
checkWinner(avgDolphins, avgKoalas);
avgDolphins = calcAverage(85, 54, 41);
avgKoalas = calcAverage(23, 34, 27);
console.log(avgDolphins, avgKoalas);
checkWinner(avgDolphins, avgKoalas);

function checkWinner(avgDolphins, avgKoalas) {
    if (avgDolphins >= avgKoalas * 2) {
        console.log(`Dolphions wins 🏆 (${avgDolphins} vs. ${avgKoalas})`);
    } else if (avgKoalas >= avgDolphins * 2) {
        console.log(`Koalas wins 🏆 (${avgKoalas} vs. ${avgDolphins})`);
    } else {
        console.log("No team wins...");
    }
} */

/* // Array
const friend1 = "Michael";
const friend2 = "Steven";
const friend3 = "Peter";
// way1 to create array
let friends = ["Michael", "Steven", "Peter"];
console.log(friends);
console.log(friends.length);
console.log(friends[friends.length - 1]);
friends[2] = "Jay";
console.log(friends);
// friends[5] = "Mike";
// console.log(friends[3]);
// console.log(friends[4]);
// console.log(friends);
// friends = ["Bob", "Alice"];
console.log(friends); // it's can be reassigned anytime in any form
// way2 to create array
// const years = new Array(1991, 1984, 2008, 2020);
// console.log(years);
// console.log(years[1]);

const firstName = "Jonas";
// an array can contain any data type
const jonas = [firstName, "Schmedtmann", 2037 - 1991, "teacher", friends];
console.log(jonas);

// Exercise
const calcAge = function (birthYear) {
    return 2037 - birthYear;
};
// we can not do directly operation to array
const years = [1990, 1967, 2002, 2010, 2018];
console.log(calcAge(years[years.length - 1]));

// Basic Array Operations (Methods)
// Add elements
const newLength = friends.push("Ray"); // push(), return the new length value of array
console.log(friends, newLength);
// unshift(), insert an element at the first position of array, and also return the new length value
const newLen = friends.unshift("John");
console.log(friends, newLen);

// Remove elements
const popped = friends.pop(); // remove the last element of array and return the removed element
console.log(friends, popped);
const shifted = friends.shift(); // remove the first element of array, and return the removed element
console.log(friends, shifted);

// return index of element
console.log(friends.indexOf("Michael"));

// Includes, verify if the element is in the array and return the boolean
friends.push(23);
console.log(friends.includes("Steven"));
console.log(friends.includes("Ray"));
console.log(friends.includes("23")); // doesn't word, includes method is in strict mode
console.log(friends.includes(23));

if (friends.includes("Steven")) {
    console.log("You have a friend called Steven");
}
 */

/* // Code Challenge 2
const calcTip = function (bill) {
    // if (bill <= 300 && bill >= 50) {
    //     return bill * 0.15;
    // } else {
    //     return bill * 0.2;
    // }
    return bill <= 300 && bill >= 50 ? bill * 0.15 : bill * 0.2;
};

const bills = [125, 555, 44];
console.log(bills);
const tips = [calcTip(bills[0]), calcTip(bills[1]), calcTip(bills[2])];
console.log(tips);
const total = [bills[0] + tips[0], bills[1] + tips[1], bills[2] + tips[2]];
console.log(total);
 */

// Object is a key-value pair
/* const jonas = {
    firstName: "Jonas",
    lastName: "Schmedtmann",
    age: 2037 - 1991,
    job: "Teacher",
    friends: ["Micheal", "Peter", "Steven"],
};

// get data from Object
console.log(jonas);
console.log(typeof jonas);
console.log(jonas.lastName);
console.log(jonas["lastName"]);

const nameKey = "Name";
console.log(jonas["first" + nameKey]);
console.log(jonas["last" + nameKey]); */

/* const interestedIn = prompt(
    "What do you want to know about Jonas ? Choose between firstName, lastName, age, job, and friends"
);
// if interestedIn is not the key value existed in object Jonas,
// jonas[interestedIn] wil return falsy value undefined
console.log(jonas[interestedIn]);
if (jonas[interestedIn]) {
    // undefined is falsy value
    console.log(jonas[interestedIn]);
} else {
    console.log(
        "Wrong request! Choose between firstName, lastName, age, job, and friends"
    );
} */

// Object operations
/* jonas.location = "Portugal";
jonas["twitter"] = "@jonasschmedtman";
console.log(jonas);

// Challenge
// "Jonas has 3 friends, and his best friend is called Micheal"
console.log(
    `${jonas.firstName} has ${jonas.friends.length} friends, and his best friend is ${jonas.friends[0]}`
); */

/* // Object methodes
const jonas = {
    firstName: "Jonas",
    lastName: "Schmedtmann",
    birthYear: 1991,
    job: "Teacher",
    friends: ["Micheal", "Peter", "Steven"],
    hasDriversLicense: false,
    // To define a function inside an Object, we need function expression rather than function declaration
    // calcAge: function (birthYear) {
    //     return 2037 - birthYear;
    // },
    // this point to the Object itself
    // calcAge: function () {
    //     // console.log(this);
    //     return 2037 - this.birthYear;
    // },
    // this point to the Object itself
    calcAge: function () {
        // console.log(this);
        this.age = 2037 - this.birthYear;
        return this.age;
    },

    getSummary: function () {
        console.log(
            `${this.firstName} is a ${this.calcAge()}-years old ${
                this.job
            }, and he has ${
                this.hasDriversLicense ? "a" : "no"
            } driver's license`
        );
    },
};

console.log(jonas.calcAge());
console.log(jonas.age);
console.log(jonas.age);
jonas.getSummary();
// console.log(jonas["calcAge"]()); */

// CODE Challenge #3
/* const mark = {
    fullName: "Mark Miller",
    mass: 78,
    height: 1.69,

    calcBMI: function () {
        this.BMI = this.mass / this.height ** 2;
        return this.BMI;
    },
};

const john = {
    fullName: "John Simth",
    mass: 92,
    height: 1.95,

    calcBMI: function () {
        this.BMI = this.mass / this.height ** 2;
        return this.BMI;
    },
};

if (mark.calcBMI() > john.calcBMI()) {
    console.log(
        `${mark.fullName}'s BMI(${mark.calcBMI()}) is higher than ${
            john.fullName
        }'s BMI(${john.calcBMI()})`
    );
} else {
    console.log(
        `${john.fullName}'s BMI(${john.calcBMI()}) is higher than ${
            mark.fullName
        }'s BMI(${mark.calcBMI()})`
    );
} */

// Loop iteration
// console.log("lifting weights, repetition 1 🏋️‍♀️");
// console.log("lifting weights, repetition 2 🏋️‍♀️");
// console.log("lifting weights, repetition 3 🏋️‍♀️");
// console.log("lifting weights, repetition 4 🏋️‍♀️");
// console.log("lifting weights, repetition 5 🏋️‍♀️");
// console.log("lifting weights, repetition 6 🏋️‍♀️");
// console.log("lifting weights, repetition 7 🏋️‍♀️");
// console.log("lifting weights, repetition 8 🏋️‍♀️");
// console.log("lifting weights, repetition 9 🏋️‍♀️");
// console.log("lifting weights, repetition 10 🏋️‍♀️");
/* for (let rep = 1; rep <= 10; rep++) {
    console.log(`lifting weights, repetition ${rep} 🏋️‍♀️`);
}

const jonas = [
    "Jonas",
    "Schmedtmann",
    1991,
    "Teacher",
    ["Micheal", "Peter", "Steven"],
    false,
];

const types = [];
// for (let i = 0; i < jonas.length; i++) {
//     // Read from jonas array
//     // console.log(jonas[i], typeof jonas[i]);
//     // Filling types array
//     // types.push(typeof jonas[i]);
//     types[i] = typeof jonas[i];
//     console.log(types[i]);
// }
// console.log(types);

const years = [1991, 2007, 1969, 2020];
const ages = [];
for (let i = 0; i < years.length; i++) {
    ages.push(2037 - years[i]);
}
console.log(ages); */
/* // Code Challenge 2
const calcTip = function (bill) {
    // if (bill <= 300 && bill >= 50) {
    //     return bill * 0.15;
    // } else {
    //     return bill * 0.2;
    // }
    return bill <= 300 && bill >= 50 ? bill * 0.15 : bill * 0.2;
};

const bills = [125, 555, 44];
console.log(bills);
const tips = [calcTip(bills[0]), calcTip(bills[1]), calcTip(bills[2])];
console.log(tips);
const total = [bills[0] + tips[0], bills[1] + tips[1], bills[2] + tips[2]];
console.log(total);
 */

// continue and break
/* console.log("--- ONLY STRING ---");
for (let i = 0; i < jonas.length; i++) {
    // Read from jonas array
    if (typeof jonas[i] !== "string") continue;
    if (typeof jonas[i] === "number") break;
    console.log(jonas[i], typeof jonas[i]);
}

console.log("--- BREAK WITH NUMBER ---");
for (let i = 0; i < jonas.length; i++) {
    // Read from jonas array
    if (typeof jonas[i] === "number") break;
    console.log(jonas[i], typeof jonas[i]);
} */

// Loop backward and loop in loop
/* const jonas = [
    "Jonas",
    "Schmedtmann",
    1991,
    "Teacher",
    ["Micheal", "Peter", "Steven"],
    false,
];

for (let i = jonas.length - 1; i >= 0; i--) {
    console.log(jonas[i], typeof jonas[i]);
    if (typeof jonas[i] === "object") {
        for (let j = 0; j < jonas[i].length; j++) {
            console.log(jonas[i][j]);
        }
    }
}

for (let exercise = 1; exercise < 4; exercise++) {
    console.log(`------- Starting Exercise ${exercise} -------`);
    for (let rep = 1; rep < 6; rep++) {
        console.log(
            `Exercise ${exercise}: Lifting weight repetition ${rep} 🏋️‍♀️`
        );
    }
} */

/* // While Loop
let rep = 1;
while (rep < 10) {
    console.log(`Lifting weight repetition ${rep} 🏋️‍♀️`);
    rep++;
}

let dice = 0;
while (dice !== 6) {
    dice = Math.trunc(Math.random() * 6) + 1;
    console.log(`You rolled a ${dice}`);
    if (dice === 6) {
        console.log(`You rolled a ${dice}, loop is about to end`);
    }
} */

// Code Challenge #4
const bills = [22, 295, 176, 440, 37, 105, 10, 1100, 86, 52];
const tips = [];
const totals = [];
function calcTiip() {
    for (let i = 0; i < bills.length; i++) {
        tips.push(
            bills[i] <= 300 && bills[i] >= 50 ? bills[i] * 0.15 : bills[i] * 0.2
        );
        totals.push(bills[i] + tips[i]);
    }
}
calcTiip();
console.log(bills);
console.log(tips);
console.log(totals);

const calcAverage = function (arr) {
    if (typeof arr !== "object") return;
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum / arr.length;
};
console.log(`The average of bills is ${calcAverage(bills)}`);
console.log(`The average of tips is ${calcAverage(tips)}`);
console.log(`The average of totals is ${calcAverage(totals)}`);
