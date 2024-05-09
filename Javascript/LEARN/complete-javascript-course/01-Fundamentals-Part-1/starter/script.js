let js = "amazing";
console.log(40 + 23 + 8 - 10);
// Values, using 'let'to define variable
// let firstName = "Jonas";
// console.log(firstName);

// Do not name a variable start with high case, unless is an Object
// Do not name a 'name' varialbe, is illeage in javascript

// Data primitive type: Javascript has dynamic typing: We do not have to manually define the data type of the value
// stored in a variable, Instead, data types are determined automatically.
// 1. Number. In javascript, all number is floating point numbers, which means they have always decimal, even
// if we don't see them or we don't define them
let age = 23;
// 2. String: Sequence of characters, in javascript, double quote and single quote have the same function
// let lastName = "Jojo";
// 3. Boolean: Logical type that can only be true or false
let fullAge = true;
// 4. Undeined: Value taken by a variable that is not yet defined (empty value)
let children; // undefined value
// 5. Null: Also means 'empty value' but not the same as undfined
let parent = null;
// 6. Symbol(ES2015): Value that is unique and cannot be changed []

// 7. BigInt (ES 2020): Larger integers than the Number type can hold

// let javascriptIsFun = true;
// console.log(typeof javascriptIsFun);
// console.log(typeof true);
// console.log(typeof 23);
// console.log(typeof "Jonas");

// javascriptIsFun = "YES!";
// console.log(typeof javascriptIsFun);

// let year; //type of undefined value is undefined, as well as it's type is undefined
// console.log(year);
// console.log(typeof year);

// year = 1991;
// console.log(year);
// console.log(typeof year);

// console.log(typeof null);

// // other 2 ways to declare variable
// // use key word 'const' to declare constant, any constant declared must have value assigned when we define them
// // and could not be changed in anytime and anycase in the future
// const age2 = 40;

// // use 'var'to define variable, it seems like using 'let', but they have many differences
// // simply saying is that, 'let' is block scoop, and 'var' is function scoop
// var job = "programmer";
// job = "teacher";

// // Operator
// const now = 2037;
// const ageJonas = now - 1991;
// const ageSarah = now - 2018;
// console.log(ageJonas, ageSarah);

// // 2 ** 3 means 2 to the power of 3 = 2 * 2 * 2
// console.log(ageJonas * 2, ageJonas / 10, 2 ** 3);

// const firstName = "Jonas";
// const lastName = "Schmedtmann";
// console.log(firstName + " " + lastName);

// Assignment operator
// let x = 10 + 5;
// x += 10; // x = x + 10 = 25
// x *= 4;
// x++;
// x--;
// x--;
// console.log((x += 10));

// Conmparison operators
console.log(ageJonas > ageSarah); // >, <, >=, <=, ===
// // console.log(ageSarah >= 18);

// // const isFullAge = ageSarah >= 18;

// // console.log(now - 1991 > now - 2019);

// // // Operator precedence
// // // Link: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence
// // let x, y;
// // x = y = 25 - 10 - 5;
// // console.log(x, y);
// // const averageAge = (ageJonas + ageSarah) / 2;
// // console.log(ageJonas, ageSarah);

// /* // Code Challenge 1
// let markMass = 78;
// let jonasMass = 92;
// let markHeight = 1.69;
// let jonasHeight = 1.95;

// let markHeigherBMI = markMass / markHeight ** 2 > jonasMass / jonasHeight ** 2;
// console.log("mark has heigher BMI: " + markHeigherBMI);

// markMass = 95;
// markHeight = 1.88;
// jonasMass = 85;
// jonasHeight = 1.76;
// markHeigherBMI = markMass / markHeight ** 2 > jonasMass / jonasHeight ** 2;
// console.log("mark has heigher BMI: " + markHeigherBMI); */

// Strings and Template Literals
const firstName = "Jonas";
const job = "teacher";
const birthYear = 1991;
const year = 2037;
const jonas =
	"I'm " +
	firstName +
	", a " +
	(year - birthYear) +
	" years old " +
	job +
	"!";
console.log(jonas);
// A better way to do that - template literals (ES6 feature)
const jonasNew = `I'm ${firstName}, a ${year - birthYear} years old ${job}!`;
console.log(jonasNew);

// // console.log(`just a regular string...`);

// // console.log(
// //   "String with \n\
// // mutiple \n\
// // lines"
// // );

// // console.log(`String with
// // mutiple
// // lines`);

// /* const age = 15;
// if (age >= 18) {
//     console.log(`Sarah can start driving license 🚗`);
// } else {
//     const yearLeft = 18 - age;
//     console.log(`Sarah is too young. Wait another ${yearLeft} years :)`);
// }

// const birthYear = 2012;
// let century;
// if (birthYear <= 2000) {
//     century = 20;
// } else {
//     century = 21;
// }
// console.log(century); */

// /* // Code Challenge 2
// let markMass = 78;
// let jonasMass = 92;
// let markHeight = 1.69;
// let jonasHeight = 1.95;
// let BMIMark = markMass / markHeight ** 2;
// let BMIJonas = jonasMass / jonasHeight ** 2;
// if (BMIMark > BMIJonas) {
//     console.log(
//         `Mark's BMI (${(markMass / markHeight ** 2).toFixed(
//             1
//         )}) is higher than John's (${(jonasMass / jonasHeight ** 2).toFixed(
//             1
//         )})`
//     );
// } else {
//     console.log(
//         `John's BMI (${(jonasMass / jonasHeight ** 2).toFixed(
//             1
//         )}) is higher than Mark's (${(markMass / markHeight ** 2).toFixed(1)})`
//     );
// }
// markMass = 95;
// markHeight = 1.88;
// jonasMass = 85;
// jonasHeight = 1.76;
// BMIMark = markMass / markHeight ** 2;
// BMIJonas = jonasMass / jonasHeight ** 2;
// if (BMIMark > BMIJonas) {
//     console.log(
//         `Mark's BMI (${(markMass / markHeight ** 2).toFixed(
//             1
//         )}) is higher than John's (${(jonasMass / jonasHeight ** 2).toFixed(
//             1
//         )})`
//     );
// } else {
//     console.log(
//         `John's BMI (${(jonasMass / jonasHeight ** 2).toFixed(
//             1
//         )}) is higher than Mark's (${(markMass / markHeight ** 2).toFixed(1)})`
//     );
// } */

/* // Type conversion
const inputYear = `1991`;
console.log(Number(inputYear) + 18); // use Number() to convert string to number
console.log(inputYear + 18);

console.log(Number(`Jonas`)); // When a string can not be logically converted to a number, Number() will return NaN
console.log(typeof NaN); // NaN is still a number, means invalid number

console.log(String(23)); // use String() convert number to string

// type coercion
console.log(`I am ${23} years old`);

console.log(`23` - `10` - 3); // minus will cause type coercion to convert string to number
console.log(`23` + `10` + 3); // plus will also cause type coercion, but it's will convert number to string
console.log(`23` * `2`); //mutiplier will cause type coercion to convert string to number
console.log(`23` / `2`); //division will cause type coercion to convert string to number

let n = `1` + 1; // plus cause type coercion to convert number to string, so the result is '11';
n = n - 1; // minus will cause type coercion to convert string to number, so the result is 11 - 1 = 10
console.log(n);

console.log(2 + 3 + 4 + `5`); // 95
console.log(`10` - 2 - `3` - `4` + `5`); // 15

// Truthy and Falsy values
// 5 falsy value in javascript: 0, '', undefined, null, NaN
console.log(Boolean(0)); // number 0
console.log(Boolean("")); // null string
console.log(Boolean(undefined)); // value undefined
console.log(Boolean(null)); // null value
console.log(Boolean(NaN)); // invalid number

// Empty Object is also true
console.log(Boolean({})); // return true

const money = 0;
if (money) {
    // money = 0 is a falsy value
    console.log("Don't spend it all ;)");
} else {
    console.log("You should get a job.");
}

let height;
if (height) {
    // undfined value is also falsy value
    console.log("YAY! Height is defined");
} else {
    console.log("Heigh is undefined");
}
// Equality Operator
const age = 18;
// '===' equality operator is a strict equality operator, and it do not do the type coercion
// Which means it's will compare value and data type
if (age === 18) {
    console.log("You just became an adult :D");
}

// '==' equality operator is loose strict equality operator, and it do the type coercion
// which means it's will only compare the value after type conversion
if ("18" == 18) {
    console.log("it is not a strict equality operator");
}

if ("18" === 18) {
    console.log("it is not a strict equality operator");
} else {
    console.log("it is a strict equality operator");
}

// A MessageBox that accept content (string) from user
const favourite = Number(prompt("What's your favourite number ?"));
console.log(favourite);
console.log(typeof favourite);
if (favourite === 23) {
    console.log("Cool! 23 is an amazing number!");
} else if (favourite === 7) {
    console.log("7 is also a cool number");
} else {
    console.log("Number is not 23 or 7");
}

if (favourite !== 23) {
    console.log("Why not 23?");
} */

/* // Boolean Logic
const hasDriveLicense = true;
const hasGoodVision = false;
console.log(hasDriveLicense && hasGoodVision);
console.log(hasDriveLicense || hasGoodVision);
console.log(!hasDriveLicense);
console.log(!hasDriveLicense && hasGoodVision);
console.log(!hasDriveLicense && !hasGoodVision);
console.log(!hasDriveLicense || !hasGoodVision);

// const shouldDrive = hasDriveLicense && hasGoodVision;
// if (shouldDrive) {
//     console.log("Sarah is able to drive!");
// } else {
//     console.log("Someone else should drive...");
// }

const isTired = true;
console.log(hasDriveLicense || hasGoodVision || isTired);

const shouldDrive = hasDriveLicense && hasGoodVision;
if (shouldDrive && !isTired) {
    console.log("Sarah is able to drive!");
} else {
    console.log("Someone else should drive...");
}

let age = 16;
if (!(age >= 20)) {
    console.log();
} else if (age >= 20 && age <= 30) {
    console.log();
} else if (age >= 20 || age <= 30) {
    console.log();
} else if (!(age >= 20) && age <= 30) {
}

// // Code Challenage 3
// let dolphinsAverageScore = (96 + 108 + 89) / 3;
// let koalasAverageScore = (88 + 91 + 110) / 3;

// if (dolphinsAverageScore > koalasAverageScore) {
//     console.log("Winner is dolphins 🏆!");
// } else {
//     console.log("Winner is koalas 🏆!");
// }

// dolphinsAverageScore = (97 + 112 + 101) / 3;
// koalasAverageScore = (109 + 95 + 123) / 3;
// if (dolphinsAverageScore > koalasAverageScore && dolphinsAverageScore >= 100) {
//     console.log("Winner is dolphins 🏆!");
// } else if (
//     koalasAverageScore > dolphinsAverageScore &&
//     koalasAverageScore >= 100
// ) {
//     console.log("Winner is koalas 🏆!");
// }

// dolphinsAverageScore = (97 + 112 + 101) / 3;
// koalasAverageScore = (109 + 95 + 106) / 3;
// if (dolphinsAverageScore > koalasAverageScore && dolphinsAverageScore >= 100) {
//     console.log("Winner is dolphins 🏆!");
// } else if (
//     koalasAverageScore > dolphinsAverageScore &&
//     koalasAverageScore >= 100
// ) {
//     console.log("Winner is koalas 🏆!");
// } else if (
//     dolphinsAverageScore === koalasAverageScore &&
//     dolphinsAverageScore >= 100 &&
//     koalasAverageScore >= 100
// ) {
//     console.log("A draw happens, no team wins the trophy 😭");
// } */
// /* // Swtich Statement
// const day = "Friday";
// switch (day) {
//     case "Monday": // day === 'Monday'
//         console.log("Plan course structure");
//         console.log("Go to coding meetup");
//         break;
//     case "Tuesday":
//         console.log("Prepare theory videos");
//         break;
//     case "Wednesday":
//     case "Thurday":
//         console.log("Write code examples");
//         break;
//     case "Friday":
//         console.log("Record Videos");
//         break;
//     case "Saturday":
//         console.log("Enjoy the weekend :D");
//         break;
//     case "Sunday":
//     default:
//         console.log("Not a valid day!");
// }
// // if replacement
// if (day === "Monday") {
//     console.log("Plan course structure");
//     console.log("Go to coding meetup");
// } else if (day === "Tuesday") {
//     console.log("Prepare theory videos");
// } else if (day === "Wednesday") {
// } else if (day === "Tuesday") {
//     console.log("Write code examples");
// } else if (day === "Friday") {
//     console.log("Record Videos");
// } else if (day === "Saturday") {
// } else if (day === "Sunday") {
//     console.log("Enjoy the weekend :D");
// } else {
//     console.log("Not a valid day!");
// }

// // Conditional(Ternary) operator
// const age = 23;
// age >= 18
//     ? console.log("I like to drink wine 🍷")
//     : console.log("I like to drink water 💧");
// const drink = age >= 18 ? "wine 🍷" : "water 💧";
// console.log(drink);

// let drink2;
// if (age >= 18) {
//     drink2 = "wine 🍷";
// } else {
//     drink2 = "water 💧";
// }

// console.log(drink2);
// console.log(`I like to drink ${age >= 18 ? "wine 🍷" : "water 💧"}`); */
// let bill = 430;
// let tip = bill >= 50 && bill <= 300 ? bill * 0.15 : bill * 0.2;
// console.log(
// 	`The bill was ${bill}, the ti was ${tip}, and the total value is ${
// 		bill + tip
// 	}`
// );
