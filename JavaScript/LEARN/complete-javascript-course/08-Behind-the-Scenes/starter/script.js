"use strict";
// 1. Execution context: variable environment and scope chain
function calcAge(birthYear) {
	const age = 2037 - birthYear;

	function printAge() {
		let output = `${firstName}, You are ${age}, born in ${birthYear}`;
		console.log(output);

		if (birthYear >= 1981 && birthYear <= 1996) {
			var millenial = true;
			// Creating NEW variable with same name as outer scope's variable
			const firstName = "Steven";
			const str = `Oh, and you're a millenial, ${firstName}`;
			console.log(str);
			function add(a, b) {
				return a + b;
			}
			// Reassigning outer scope's variable
			output = "NEW OUTPUT";
		}
		// console.log(str); error, str is defined in block scope and can not be access outside the block
		// millenial is define in block scope, but using 'var' to define, so it's accessable outside the block scope
		console.log(millenial);
		// error, function definition is also not access outside the block
		// add(2, 3);
		console.log(output);
	}
	printAge();
	return age;
}

const firstName = "Jonas";
calcAge(1991);
// console.log(age); can not access age vairable
// pinrtAge() is also not accessable */

/* // 2. Hoisting and TDZ
// Variable
// console.log(me); // cause undefined error
// console.log(job); // cause 'reference error'
// console.log(year);
var me = "Jonas";
let job = "teacher";
const year = 1991;

// Function
console.log(addDecl(2, 3)); // no error, function declaration will be hoisted, so function could be called before definition
// console.log(addExpr(2, 3)); // error, function expression is simply a const variable and  won't be hoisted, could not be called before definition
// console.log(addArrow(2, 3)); // error, even we define function using var which will be hoisted, as var variable is undefined here, it will cause undefine error
function addDecl(a, b) {
	return a + b;
}

const addExpr = function (a, b) {
	return a + b;
};

var addArrow = (a, b) => a + b;

// Example
if (!numProducts) deleteShoppingCart(); // numProducts is undefined product right now
var numProducts = 10;
function deleteShoppingCart() {
	console.log("All products deleted");
}
// Conclusion: DON'T USE 'var' to declare function or variable

var x = 1; // using 'var' will create window property.
let y = 2;
const z = 3;
console.log(x === window.x);
console.log(y === window.y);
console.log(z === window.z); */

/* // 'this' keyword
console.log(this); // this in global is window
const calcAge = function (birthYear) {
	console.log(2037 - birthYear);
	console.log(this); // this is undefined in a declared function
};
calcAge(1991);

const calcAgeArrow = (birthYear) => {
	console.log(2037 - birthYear);
	console.log(this); // in arrow function, this keyword will point to surraround this object
};
calcAgeArrow(1991);

const jonas = {
	year: 1991,
	calcAge: function () {
		console.log(this); // here 'this' point to the object which calling this method
		console.log(2037 - this.year);
	},
};
jonas.calcAge();
const matilda = {
	year: 2017,
};

matilda.calcAge = jonas.calcAge;
matilda.calcAge();

const f = jonas.calcAge;
// f(); // this regular fucntion called, this keyword is undefined
 */

// Regular function vs. arrow function
// var firstName = "Metilda";

const jonas = {
	firstName: "Jonas",
	year: 1991,
	calcAge: function () {
		console.log(this); // here 'this' point to the object which calling this method
		console.log(2037 - this.year);
		// even it's defined in a object method, here this regular function is considered as an normal regular function, so this won't point to any object as if a regular function defined in global
		// const isMellenial = function () {
		// 	console.log(this.year >= 1981 && this.year <= 1996);
		// };
		// Solution 1, use another variable to save this
		// But if we use another variable to save this, and use this variable in a regular function, it will work.
		// const self = this;
		// const isMellenial = function () {
		// 	console.log(self.year >= 1981 && self.year <= 1996);
		// };
		// Solution 2, use arrow function
		// But a better solution in ES6 is to use arrow function
		const isMellenial = () => {
			console.log(this.year >= 1981 && this.year <= 1996);
		};
		isMellenial();
	},
	// greet: () => console.log(`Hey ${this.firstName}`), // in arrow function, 'this' keyword always point to the object surrarounded
	greet: function () {
		console.log(`Hey ${this.firstName}`);
	},
};
jonas.greet();
jonas.calcAge();

// arguments keyword
const addExpr = function (a, b) {
	console.log(arguments);
	return a + b;
};
addExpr(2, 3);
addExpr(2, 5, 8, 10);

// arrow function does not have 'arguments' keyword
var addArrow = (a, b) => {
	console.log(arguments);
	return a + b;
};

// addArrow(2, 3, 5, 6); //Error: arguments is undefined

// PRIMITIVES vs. OBJECTS (Primitive vs. reference types)
// Primitive data is Number | String | Boolean | Undefined | Null | Symbol | BigInt they are stored in CALL Stack
// Object means Object literal | Arrays | Functions and etc are stored in HEAP
// In the eample below, both age/oldAge/me/friend are primitive data that stroed in CALL STACK, however for me and friend, as they are actualy stored an object data that should stored in HEAD, So me and friend this two primitive data are actually stored the same address of object data in HEAD (which means they point to the same object), So when we changed age value by using friend.age, it will havs the same functionality of me.age, because they stored the same address.
// That is also why we can change the attibute value of object that defiend with const, as we are actually changing the value that stored in HEAD , rather than the value stored with const (it's an address)
// Primitive type
let age = 30;
let oldAge = age;
age = 31;
console.log(age);
console.log(oldAge);

// Reference type
const me = {
	name: "Jonas",
	age: 30,
};

const friend = me;
friend.age = 27;
console.log("Me:", me);
console.log("Friend:", friend);

// Practice PRIMITIVES vs. OBJECTS (Primitive vs. reference types)
// Primitive type
let lastName = "Williams";
let oldLastName = lastName;
lastName = "Davis";
console.log(lastName, oldLastName);

// Reference type
const jessica = {
	firstName: "Jessica",
	lastName: "Williams",
	age: 27,
};

const marriedJessica = jessica;
marriedJessica.lastName = "Davis";
console.log("Before marriage:", jessica);
console.log("After marriage:", marriedJessica);

// marriedJessica = {}; // since it's an const any already assigned, it can not be changed any longer

// A way to copy an object and change it's attribute without changing the original one
// Copying Object -> using Ojbect.assign({}, Object)
const jessica2 = {
	firstName: "Jessica",
	lastName: "Williams",
	age: 27,
	family: ["Alice", "Bob"],
};
// Object.assgin() has a problem which is that when the object to be copied has an inner object, the inner object can not be changed in the return object, which means, Object.assign() only create a shallow copy, that means they only copy property in first level
const jessicaCopy = Object.assign({}, jessica2);
jessicaCopy.family.push("Mary"); // this part won't have difference
jessicaCopy.family.push("John"); // this part won't have difference
jessicaCopy.lastName = "Davis";
console.log("Before marriage:", jessica2);
console.log("After marriage:", jessicaCopy);
