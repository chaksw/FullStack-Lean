"use strict";

// Data needed for a later exercise
const flights =
	"_Delayed_Departure;fao93766109;txl2133758440;11:25+_Arrival;bru0943384722;fao93766109;11:45+_Delayed_Arrival;hel7439299980;fao93766109;12:05+_Departure;fao93766109;lis2323639855;12:30";

// Data needed for first part of the section
const restaurant = {
	name: "Classico Italiano",
	location: "Via Angelo Tavanti 23, Firenze, Italy",
	categories: ["Italian", "Pizzeria", "Vegetarian", "Organic"],
	starterMenu: ["Focaccia", "Bruschetta", "Garlic Bread", "Caprese Salad"],
	mainMenu: ["Pizza", "Pasta", "Risotto"],

	openingHours: {
		thu: {
			open: 12,
			close: 22,
		},
		fri: {
			open: 11,
			close: 23,
		},
		sat: {
			open: 0, // Open 24 hours
			close: 24,
		},
	},

	order: function (starterIndex, mainIndex) {
		return [this.starterMenu[starterIndex], this.mainMenu[mainIndex]];
	},
	// execute destructuring in function
	// using element name of object as parameters in function, when using an object as parameter to call this function, it will destruct the object first to get the element's value, and then pass this values to function to execute logic
	// In that case, we do not need to worry about the order of element in object
	// Also we can set the default value for this parameter, so that we can simply pass the parameter we want into this function, then the rest parameter will remain default
	orderDelivery: function ({
		starterIndex = 1,
		mainIndex = 0,
		time = "20:00",
		address,
	}) {
		console.log(
			`Order received! ${this.starterMenu[starterIndex]} and ${this.mainMenu[mainIndex]} will be delivered to ${address} at ${time} `
		);
	},

	orderPasta: function (ing1, ing2, ing3) {
		console.log(
			`Here is your delicious pasta with ${ing1},${ing2},${ing2}`
		);
	},

	orderPizza: function (mainIngredient, ...otherIngredients) {
		console.log(mainIngredient);
		console.log(otherIngredients);
	},
};

// 1. Desctructuring

/////////////////////////////////////
// Destructuring Arrays
const arr = [2, 3, 4];
const a = arr[0];
const b = arr[1];
const c = arr[2];

/// Save array value in destructuring way
const [x, y, z] = arr;

// If we want only get the first and third valu of categories
let [main, , seconary] = restaurant.categories;
console.log(main, seconary);

// Swtich value in a normal way
const temp = main;
main = seconary;
seconary = temp;
console.log(main, seconary);

// Swtich with destructuring
[main, seconary] = [seconary, main];
console.log(main, seconary);
// return multiple value from function using destructuring
const [starter, mainCourse] = restaurant.order(2, 0);
console.log([starter, mainCourse]);

// nested destructuring
const nested = [2, 4, [5, 6]];
// Get inner array's value using destructuring
const [i, , [j, k]] = nested;
console.log(i, j, k);

// Set default value
const [p = 1, q = 1, r = 1] = [8, 9];
console.log(p, q, r);

const order = {
	time: "22:30",
	address: "Via del Sole, 21",
	mainIndex: 2,
	starterIndex: 2,
};

/* 
////////////////////////
// Desturcturing Objects
// we can simply use the object's element as left value to destructuring the elements in the obejct
const { name, openingHours, categories } = restaurant;
console.log(name, openingHours, categories);
// If we want the variable name different with the property name of object
// get the original property name and using ':' to separate the variable name
const {
	name: restaurantName,
	openingHours: Hours,
	categories: tags,
} = restaurant;
console.log(restaurantName, Hours, tags);

// Default Value, if the property existed in object, the default value will be replaced by property value
// other wise like menu below, new variable will remain default value
// if we didn't define default value, the new variable will remain undefined
const { menu = [], starterMenu: starters = [] } = restaurant;
console.log(menu, starters);

// Mutating (改变) variales
let a = 111;
let b = 999;
// Mutating a and b with obj
const obj = { a: 23, b: 7, c: 14 };
// we need add a parenthseis
({ a, b } = obj);
console.log(a, b);

// Nested(内嵌) Object
// Destructuring openingHours first to find the 'fri' element, then destructuring 'fri' object to get the 'open' and 'close' element, and finally reassign (or rename) as 'o' and 'c'
const {
	fri: { open: o, close: c },
} = openingHours;
console.log(o, c); 

restaurant.orderDelivery(order);

// restaurant.orderDelivery({
// 	time: "22:30",
// 	address: "Via del Sole, 21",
// 	mainIndex: 2,
// 	starterIndex: 2,
// });
restaurant.orderDelivery({ address: '"Via del Sole, 21"', starterIndex: 1 });
*/

////////////////////////
// Short circuiting Or and ___
// Use ANY data type, return ANY data type, short-circuiting
// return the first true value, otherwise return the last value,
// 总之就是返回第一个真值，如果没有真值就返回最后一个值
console.log("----------- OR ----------");
console.log(3 || "Jonas"); // 3
console.log("" || "Jonas"); // "Jonas"
console.log(true || 0); // true
console.log(undefined || null); // null

console.log(undefined || 0 || "" || "Hello" || 23 || null);

// restaurant.numGuests = 23;
const guests1 = restaurant.numGuests ? restaurant.numGuests : 10;
console.log(guests1);
// if there is no restaurant.numGuests or it's 0, it will return 10, otherwise it will return restaurant.numGuests
const guests2 = restaurant.numGuests || 10;
console.log(guests2);

console.log("----------- AND ----------");
// And operator works in the opposite way of the OR operator
// return the first falsy value, otherwise return the last value,
// 总之就是返回第一个假值，如果没有假值就返回最后一个值
console.log(0 && "Jonas");
console.log(7 && "Jonas");
console.log(7 && 0);
console.log("Hello" && 23 && null && "Jonas");

if (restaurant.orderPizza) {
	restaurant.orderPizza("mushrooms", "spinach");
}
// We can put any thing with && or || operator, not just a value
// If the function existed, execute the function
restaurant.orderPizza && restaurant.orderPizza("mushrooms", "spinach");

/* ////////////////////////
// Rest Pattern
// 1) Destructuring
// the spread opertor use to unpack an array (separate element), but rest pattern use to pack element into an array
// SPREAD, because on RIGHT side of =
const arr = [1, 2, ...[3, 4]];
// REST, because on LEFT side of =
const [a, b, ...others] = [1, 2, 3, 4, 5];
console.log(a, b, others);
// The rest element must be the last element and can be only used once
const [pizza, , risotto, ...otherFood] = [
	...restaurant.mainMenu,
	...restaurant.starterMenu,
];
console.log(pizza, risotto, otherFood);

// Objects
const { sat, ...weekDays } = restaurant.openingHours;
console.log(sat, weekDays);

// 2) Functions
const add = function (...numbers) {
	let sum = 0;
	for (let i = 0; i < numbers.length; i++) sum += numbers[i];
	console.log(sum);
};
add(2, 3);
add(5, 3, 7, 2);
add(8, 2, 5, 3, 2, 1, 4);

const x = [23, 5, 7];
add(...x);

restaurant.orderPizza("mushrooms", "onion", "olives", "spinach");
restaurant.orderPizza("mushrooms");
 */
/* ///////////////////////////////////////
// The spread (传播) operator (...)
const arr = [7, 8, 9];
const badNewArr = [1, 2, arr[0], arr[1], arr[2]];
console.log(badNewArr);
// Use spread operator to expend array
// the spread operator is used to take all the element out of the array, and write them manually(element sparated by comma)
const newArr = [1, 2, ...arr];
console.log(newArr);

// use directly in an array, it will take all the element out
console.log(...newArr);

const newMenu = [...restaurant.mainMenu, "Gnocci"];
console.log(newMenu);

// Copy array
const newMenuCopy = [...restaurant.mainMenu];

// Join 2 arrays
const menu = [...restaurant.starterMenu, ...restaurant.mainMenu];
console.log(menu);

// Iterables: array, strings, maps, sets. NOT objects
const str = "Jonas";
const letters = [...str, "", "S."];
console.log(letters);

// Real world example
// const ingredients = [
// 	prompt("Let's make pasta! Ingredient 1?"),
// 	prompt("Ingredient 2?"),
// 	prompt("Ingredient 3?"),
// ];

// console.log(ingredients);
// restaurant.orderPasta(...ingredients);

// Use spread operaotr in Objects
const newRestaurant = { foundedIn: 1998, ...restaurant, founder: "Guisepe" };
console.log(newRestaurant);

// Shallow copy of object using spread operator
const restaurantCopy = { ...restaurant };
restaurantCopy.name = "Rsitorante Roma";
console.log(restaurantCopy.name);
console.log(restaurant.name); */
