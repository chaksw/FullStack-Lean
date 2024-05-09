- [1. What is Javascript](#1-what-is-javascript)
  - [1. HIGH-LEVEL](#1-high-level)
    - [1.1.1. Garbage-collected](#111-garbage-collected)
    - [1.1.2. Interpreted or Just-In-Time compiled](#112-interpreted-or-just-in-time-compiled)
  - [1.2. Multi-paradigm (多范式)](#12-multi-paradigm-多范式)
  - [1.3. PROTOTYPE-BASE Object-oriented](#13-prototype-base-object-oriented)
  - [1.4. First-Class function](#14-first-class-function)
  - [1.5. Dynamic](#15-dynamic)
  - [1.6. Single-threaded （单线程）\& Non-blocking event loop concurrency model（非阻塞事件循环并发模型）](#16-single-threaded-单线程-non-blocking-event-loop-concurrency-model非阻塞事件循环并发模型)
- [2. Principle](#2-principle)
  - [2.1. Data primitive type](#21-data-primitive-type)
  - [2.2. Other 2 ways to declare variable: `const`, `var`](#22-other-2-ways-to-declare-variable-const-var)
  - [2.3. Operator](#23-operator)
    - [2.3.1. Assignment operator](#231-assignment-operator)
    - [2.3.2. Conmparison operators](#232-conmparison-operators)
  - [2.4. Strings and Template Literals](#24-strings-and-template-literals)
  - [2.5. Type conversion `Number()`, `String()`](#25-type-conversion-number-string)
    - [2.5.1. Type coercion](#251-type-coercion)
    - [2.5.2. Exmaple](#252-exmaple)
  - [2.6. Truthy and Falsy values](#26-truthy-and-falsy-values)
    - [2.6.1. Example](#261-example)
  - [2.7. Equality Operator `===`, `==`](#27-equality-operator--)
  - [2.8. A MessageBox that accept content (string) from user](#28-a-messagebox-that-accept-content-string-from-user)
  - [2.9. Boolean Logic `&&`, `||`, `!`](#29-boolean-logic---)
  - [2.10. `use strict`](#210-use-strict)
  - [2.11. Function](#211-function)
    - [2.11.1. Function declaration](#2111-function-declaration)
    - [2.11.2. Function expression (Anonymity function)](#2112-function-expression-anonymity-function)
    - [2.11.3. Arrow function](#2113-arrow-function)
      - [2.11.3.1. Arrow function with multiple parameter](#21131-arrow-function-with-multiple-parameter)
    - [2.11.4. Functions calling other functions](#2114-functions-calling-other-functions)
  - [2.12. Array](#212-array)
    - [2.12.1. Way 1 to create array](#2121-way-1-to-create-array)
    - [2.12.2. Way 2 to create array](#2122-way-2-to-create-array)
    - [2.12.3. Basic Array Operations (Methods)](#2123-basic-array-operations-methods)
  - [2.13. Object](#213-object)
    - [2.13.1. Object methodes](#2131-object-methodes)
  - [2.14. Loop iteration](#214-loop-iteration)
    - [2.14.1. Example](#2141-example)
  - [2.15. `continue` and `break`](#215-continue-and-break)
  - [2.16. Loop backward and loop in loop](#216-loop-backward-and-loop-in-loop)
  - [2.17. `while` Loop](#217-while-loop)
  - [2.18. Regular function vs. Arrow function in using `this`](#218-regular-function-vs-arrow-function-in-using-this)
  - [2.19. PRIMITIVES vs. OBJECTS (Primitive vs. reference types)](#219-primitives-vs-objects-primitive-vs-reference-types)
  - [2.20. Data Structures Operators](#220-data-structures-operators)
    - [2.20.1. Using element name of object as parameters in function](#2201-using-element-name-of-object-as-parameters-in-function)
      - [2.20.1.1. Example](#22011-example)
  - [2.21. Desctructuring](#221-desctructuring)
    - [2.21.1. Destructuring Arrays](#2211-destructuring-arrays)
    - [2.21.2. Desturcturing Objects](#2212-desturcturing-objects)
      - [2.21.2.1. Nested(内嵌) Object](#22121-nested内嵌-object)
      - [2.21.2.2. Use Object as parameter in object function](#22122-use-object-as-parameter-in-object-function)

# 1. What is Javascript

Javascript is a HIGH-LEVEL, PROTOTYPE-BASE OBJECT-ORIENTED, MULTI-PARADIGM, INTERPRETED OR JUEST-IN-TIME COMPLIED, DYNAMIC, SIGNLE-THRAEDED, GARBAGA-COLLECTED PROGRAMMING LANGUAGE with first-class functions and a non-blocking event loop concurrency model

## 1. HIGH-LEVEL

高级语言意味着 Javascript 不需要像 C/C++那般仔细地通过代码实现硬件/内存资源的管理，而是借助于语言本身的内部内存管理机制自动管理，带来的结果就是 JavaScript 运行时间永远不能比 C/C++快，也无法进行内存优化。

### 1.1.1. Garbage-collected

其中一个 JavaScirpt 内存管理工具成为垃圾回收，即 JavaScipt 会自动删除旧的和未使用的对象。
PS: JavaScript 中几乎所有的东西（数组，函数）都是对象（Object)，(字符串，数字不是)

### 1.1.2. Interpreted or Just-In-Time compiled

## 1.2. Multi-paradigm (多范式)

Paradiugm: An approach and mindset of structuring code, which will direct your coding style and technique
(范式是指代码格式)
JavaScirpt 多种代码范式，一般的范式分为：

1. Procedural Programming (程序化编程)
2. Object-oriented programming (OOP) （面向对象编程）
3. Functional programming （函数式编程，即基于函数的代码编程）

另外一种分类方式为：

1. Imperative (命令式)
2. Declarative （声明式）

## 1.3. PROTOTYPE-BASE Object-oriented

JavaScript 中几乎所有的东西（数组，函数）都是对象（Object)，(字符串，数字不是), 而对象的创建是通过原型继承（prototype-inheritance)实现的, 原型中包含了对象可调用的方法

<div align="center">
<img src="https://github.com/chaksw/Javascript-Beginner/blob/main/imgs/Prototype-base.png?raw=true" width=80%>
</div>

## 1.4. First-Class function

函数在 JavaScript 中被视为常规变量，也意味着它们可以被当作另一个函数函数的输入参数，也可以作为函数的返回值

<div align="center">
<img src=https://github.com/chaksw/Javascript-Beginner/blob/main/imgs/first-class-fcuntion.png?raw=true" width=80%>
</div>

## 1.5. Dynamic

在 JavaScript 的变量为动态变量 （弱类型语言），也就是说变量可以定义为任何变量类型，因此一个变量可以被赋值为整形，浮点型，字符串。而 JavaScript Engine 只有在代码执行阶段才会确认变量类型。
PS：typescript 为强类型语言，即需要在定义变量时声明变量类型

## 1.6. Single-threaded （单线程）& Non-blocking event loop concurrency model（非阻塞事件循环并发模型）

JavaScript 本身运行在一个单线程中，（一次只能执行一个指令（处理器执行代码）），所以我们需要一个处理多个任务同时出现的场景的手段，这就是 Non-blocking event loop concurrency model（非阻塞事件循环并发模型），简单来说就是将一些任务（如数据处理）放在后台执行，在这些任务执行完毕后。

# 2. Principle

-   Values, using 'let'to define variable

```js
let firstName = "Jonas";
console.log(firstName);
```

-   Do not name a variable start with **high case**, unless is an Object
-   Do not name a `name` varialbe, is illeage in javascript

## 2.1. Data primitive type

Javascript has dynamic typing: We do not have to manually define the data type of the value stored in a variable, Instead, data types are determined automatically.

1. Number. In javascript, all number is floating point numbers, which means they have always decimal, even
   if we don't see them or we don't define them

```js
let age = 23;
```

1. `String`: Sequence of characters, in javascript, double quote and single quote have the same function

```js
let lastName = "Jojo";
```

2. `Boolean`: Logical type that can only be true or false

```js
let fullAge = true;
```

3. `Undeined`: Value taken by a variable that is not yet defined (empty value)

```js
let children; undefined value
```

4. `Null`: Also means 'empty value' but not the same as undfined

```js
let parent = null;
```

5. `Symbol`(ES2015): Value that is unique and cannot be changed []

6. `BigInt` (ES 2020): Larger integers than the Number type can hold

## 2.2. Other 2 ways to declare variable: `const`, `var`

1. use key word `const` to declare constant, any constant declared must have value assigned when we define them and could not be changed in anytime and anycase in the future.

```js
const age2 = 40;
```

2. set `var` to define variable, it seems like using `let`, but they have different scope chain, `let` is block scoop, and `var` is function scoop

NOTE:

-   当 `var` 变量在函数外部声明时，作用域是全局的。这意味着在函数体外用 `var` 声明的任何变量都可以在整个窗口中使用。
-   `var` 在函数中声明时，它的作用域是在函数体内。这意味着它只能在该函数中被访问
-   `var` 变量可以重新声明和更新, 并不会导致出错， 但 `let` 定义后只能更新不能重新声明， `const` 定义后不能更新或者重新声明

```js
var greeter = "hey hi";
var greeter = "say Hello instead";
```

```js
var job = "programmer";
```

## 2.3. Operator

### 2.3.1. Assignment operator

```js
let x = 10 + 5;
x += 10; // x = x + 10 = 25
x *= 4;
x++;
x--;
x--;
```

### 2.3.2. Conmparison operators

```js
console.log(ageJonas > ageSarah); // >, <, >=, <=
```

## 2.4. Strings and Template Literals

```js
const firstName = "Jonas";
const job = "teacher";
const birthYear = 1991;
const year = 2037;
const jonas = "I'm " + firstName + ", a " + (year - birthYear) + " years old " + job + "!";
console.log(jonas);
// A better way to do that - template literals (ES6 feature)
const jonasNew = `I'm ${firstName}, a ${year - birthYear} years old ${job}!`;
console.log(jonasNew);
```

## 2.5. Type conversion `Number()`, `String()`

use `Number()` to convert string

```js
const inputYear = `1991`;
console.log(Number(inputYear) + 18); // to number
console.log(inputYear + 18);
```

When a string can not be logically converted to a number, `Number()` will return `NaN`, `NaN` is still a number, means invalid number

```js
console.log(Number(`Jonas`));
console.log(typeof NaN); //
```

use `String()` convert number to string

```js
console.log(String(23)); //
```

### 2.5.1. Type coercion

-   minus(`-`) will cause type coercion to convert string to number

```js
console.log(`I am ${23} years old`);
console.log(`23` - `10` - 3);
```

-   plus(`+`) will also cause type coercion, but it's will convert number to string

```js
console.log(`23` + `10` + 3);
```

-   mutiplier(`*`) will cause type coercion to convert string to number

```js
console.log(`23` * `2`);
```

-   division(`/`) will cause type coercion to convert string to number

```js
console.log(`23` / `2`);
```

### 2.5.2. Exmaple

```js
let n = `1` + 1; // plus cause type coercion to convert number to string, so the result is '11';
n = n - 1; // minus will cause type coercion to convert string to number, so the result is 11 - 1 = 10
console.log(n);
console.log(2 + 3 + 4 + `5`); // 95
console.log(`10` - 2 - `3` - `4` + `5`); // 15
```

## 2.6. Truthy and Falsy values

Five **falsy** value in javascript: `0`, `''`, `undefined`, `null`, `NaN`

```js
console.log(Boolean(0)); // number 0
console.log(Boolean("")); // null string
console.log(Boolean(undefined)); // value undefined
console.log(Boolean(null)); // null value
console.log(Boolean(NaN)); // invalid number
```

**NOTE:** Empty Object is also true

```js
console.log(Boolean({})); // return true
```

### 2.6.1. Example

```js
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
```

## 2.7. Equality Operator `===`, `==`

`===` equality operator is a strict equality operator, and it do not do the type coercio, which means it's will compare value and data type

```js
const age = 18;
if (age === 18) {
    console.log("You just became an adult :D");
}
```

`==` equality operator is loose strict equality operator, and it do the type coercion, which means i**t's will only compare the value after type conversion**

```js
if ("18" == 18) {
    console.log("it is not a strict equality operator");
}

if ("18" === 18) {
    console.log("it is not a strict equality operator");
} else {
    console.log("it is a strict equality operator");
}
```

## 2.8. A MessageBox that accept content (string) from user

```js
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
}
```

## 2.9. Boolean Logic `&&`, `||`, `!`

```js
const hasDriveLicense = true;
const hasGoodVision = false;
console.log(hasDriveLicense && hasGoodVision);
console.log(hasDriveLicense || hasGoodVision);
console.log(!hasDriveLicense);
console.log(!hasDriveLicense && hasGoodVision);
console.log(!hasDriveLicense && !hasGoodVision);
console.log(!hasDriveLicense || !hasGoodVision);

const shouldDrive = hasDriveLicense && hasGoodVision;
if (shouldDrive) {
    console.log("Sarah is able to drive!");
} else {
    console.log("Someone else should drive...");
}

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
```

## 2.10. `use strict`

During development, we need to use the uptodate Google Chrome to ensure our code could be used in the latest javascript standard. <br>
After developpment, to ensure our development could be used in any versioin of browser we use Babel to transpile and polyfill code (converting back to ES5 to ensure browser compatibility for all users)<br>
Some word (variable name) is reserved, in strict mode, defining them will cause `syntaxError` but without declaration of 'use strict', this kind of error will not show

## 2.11. Function

In using function declaration, function could be called before its'definition, but we could not called the function expresiion before defining it.

### 2.11.1. Function declaration

```js
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

function calcAge1(birthYear) {
    // const age = 2037 - birthYear;
    // return age;
    return 2037 - birthYear;
}

const age1 = calcAge1(1991);
console.log(age1);
```

### 2.11.2. Function expression (Anonymity function)

Anonymity function, also called function expression

```js
const calcAge2 = function (birthYear) {
    return 2037 - birthYear;
};

const age2 = calcAge2(1991);
console.log(age1, age2);
```

### 2.11.3. Arrow function

Arrow function, it's a function expression, the return value is implicit in this function, `birthYear` is input parameter, and the return value is implicit (2037 - birthYear)

-   Arrow function with parameter

```js
const calcAge3 = (birthYear) => 2037 - birthYear;
const age3 = calcAge3(2000);
console.log(age3);

Arrow function with parameter
const yearUntilRetirement = (birthYear) => {
    const age = 2037 - birthYear;
    const retirement = 65 - age;
    return retirement;
};

console.log(yearUntilRetirement(1991));
```

#### 2.11.3.1. Arrow function with multiple parameter

```js
const yearUntilRetirement = (birthYear, firstName) => {
    const age = 2037 - birthYear;
    const retirement = 65 - age;
    return `${firstName} retires in ${retirement} years`;
};

console.log(yearUntilRetirement(1991, "Jonas"));
console.log(yearUntilRetirement(1980, "Bob")); */
```

### 2.11.4. Functions calling other functions

```js
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
```

## 2.12. Array

### 2.12.1. Way 1 to create array

```js
let friends = ["Michael", "Steven", "Peter"];
console.log(friends);
console.log(friends.length);
console.log(friends[friends.length - 1]);
friends[2] = "Jay";
console.log(friends);
```

It's can be reassigned anytime in any form

```js
friends[5] = "Mike";
console.log(friends[3]);
console.log(friends[4]);
console.log(friends);
friends = ["Bob", "Alice"];
console.log(friends); //
```

### 2.12.2. Way 2 to create array

An array can contain any data type

```js
const years = new Array(1991, 1984, 2008, 2020);
console.log(years);
console.log(years[1]);

const firstName = "Jonas";
// an array can contain any data type
const jonas = [firstName, "Schmedtmann", 2037 - 1991, "teacher", friends];
console.log(jonas);
```

### 2.12.3. Basic Array Operations (Methods)

1. Add elements `push`

```js
// Add elements
const newLength = friends.push("Ray"); // push(), return the new length value of array
console.log(friends, newLength);
// unshift(), insert an element at the first position of array, and also return the new length value
const newLen = friends.unshift("John");
console.log(friends, newLen);
```

2. Remove elements `pop`, `shift`

-   Use `pop` to remove the **last** element of array and return the removed element
-   Use `shift` to emove the **first** element of array, and return the removed element

```js
// Remove elements
const popped = friends.pop(); // remove the last element of array and return the removed element
console.log(friends, popped);
const shifted = friends.shift(); // remove the first element of array, and return the removed element
console.log(friends, shifted);
```

3. Return index of element `indexof`

```js
// return index of element
console.log(friends.indexOf("Michael"));
```

4. `includes`

Verify if the element is in the array and return the boolean

```js
// Includes, verify if the element is in the array and return the boolean
friends.push(23);
console.log(friends.includes("Steven"));
console.log(friends.includes("Ray"));
console.log(friends.includes("23")); // doesn't word, includes method is in strict mode
console.log(friends.includes(23));

if (friends.includes("Steven")) {
    console.log("You have a friend called Steven");
}
```

## 2.13. Object

Object is a **key-value** pair

```js
const jonas = {
    firstName: "Jonas",
    lastName: "Schmedtmann",
    age: 2037 - 1991,
    job: "Teacher",
    friends: ["Micheal", "Peter", "Steven"],
};
```

-   Get data from Object

```js
// get data from Object
console.log(jonas);
console.log(typeof jonas);
console.log(jonas.lastName);
console.log(jonas["lastName"]);

const nameKey = "Name";
console.log(jonas["first" + nameKey]);
console.log(jonas["last" + nameKey]); */

const interestedIn = prompt(
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
}
```

-   Object operations

```js
// Object operations
jonas.location = "Portugal";
jonas["twitter"] = "@jonasschmedtman";
console.log(jonas);
```

### 2.13.1. Object methodes

```js
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
            `${this.firstName} is a ${this.calcAge()}-years old ${this.job}, and he has ${
                this.hasDriversLicense ? "a" : "no"
            } driver's license`
        );
    },
};

console.log(jonas.calcAge());
console.log(jonas.age);
console.log(jonas.age);
jonas.getSummary();
// console.log(jonas["calcAge"]());
```

## 2.14. Loop iteration

```js
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
for (let rep = 1; rep <= 10; rep++) {
    console.log(`lifting weights, repetition ${rep} 🏋️‍♀️`);
}
```

### 2.14.1. Example

```js
const jonas = ["Jonas", "Schmedtmann", 1991, "Teacher", ["Micheal", "Peter", "Steven"], false];

const types = [];
for (let i = 0; i < jonas.length; i++) {
    // Read from jonas array
    // console.log(jonas[i], typeof jonas[i]);
    // Filling types array
    // types.push(typeof jonas[i]);
    types[i] = typeof jonas[i];
    console.log(types[i]);
}
console.log(types);

const years = [1991, 2007, 1969, 2020];
const ages = [];
for (let i = 0; i < years.length; i++) {
    ages.push(2037 - years[i]);
}
console.log(ages);
```

## 2.15. `continue` and `break`

```js
console.log("--- ONLY STRING ---");
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
}
```

## 2.16. Loop backward and loop in loop

```js
const jonas = ["Jonas", "Schmedtmann", 1991, "Teacher", ["Micheal", "Peter", "Steven"], false];

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
        console.log(`Exercise ${exercise}: Lifting weight repetition ${rep} 🏋️‍♀️`);
    }
}
```

## 2.17. `while` Loop

```js
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
}
```

## 2.18. Regular function vs. Arrow function in using `this`

While defined a regular function in an object, `this` inside the function won't point to any object as if a regular function defined in global. So to use `this` as object inside an object function, a better solution is to define an Arrow function.
NOTE: Arrow function don't have `arguments` key word, `arguments` 是一个类数组的对象, 其表示了函数执行时传入函数的所有参数

```js
const jonas = {
    firstName: "Jonas",
    year: 1991,
    calcAge: function () {
        console.log(this); // here 'this' point to the object which calling this method
        console.log(2037 - this.year);
        // even it's defined in a object method, here this regular function is considered as an normal regular function, so this won't point to any object as if a regular function defined in global
        const isMellenial = function () {
            // Here this point to nothing
            console.log(this.year >= 1981 && this.year <= 1996);
        };
        // Solution 1, use another variable to save this
        // But if we use another variable to save this, and use this variable in a regular function, it will work.
        const self = this;
        const isMellenial = function () {
            console.log(self.year >= 1981 && self.year <= 1996);
        };
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
```

## 2.19. PRIMITIVES vs. OBJECTS (Primitive vs. reference types)

Primitive data is `Number` | `String` | `Boolean` | `Undefined` | `Null` | `Symbol` | `BigInt`,they are stored in CALL Stack(调用栈)<br>
Object means Object `literal` | `Arrays` | `Functions` and etc are stored in HEAP(堆)<br>
In the eample below, both `age`/`oldAge`/`me`/`friend` are primitive data that stroed in CALL STACK, however for `me` and `friend`, as they are actualy stored an object data that should stored in HEAD, So `me` and `friend` this two primitive data are actually stored the same address of object data in HEAD (which means they point to the same object), So when we changed `age` value in `me` by using `friend.age`, it will havs the same functionality of `me.age`, because they stored the same address.<br>
That is also why we can change the attibute value of object that defiend with `const`, as we are actually changing the value that stored in HEAD , rather than the value stored with const (it's an address)

```js
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
```

## 2.20. Data Structures Operators

### 2.20.1. Using element name of object as parameters in function

when using an object as parameter to call this function, it will **destruct** the object first to get the element's value, and then pass this values to function to execute logic.<br>
In that case, we do not need to worry about the order of element in object, also we can set the default value for this parameter, so that we can simply pass the parameter we want into this function, then the rest parameter will remain default

#### 2.20.1.1. Example

```js
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
    orderDelivery: function ({ starterIndex = 1, mainIndex = 0, time = "20:00", address }) {
        console.log(
            `Order received! ${this.starterMenu[starterIndex]} and ${this.mainMenu[mainIndex]} will be delivered to ${address} at ${time} `
        );
    },

    orderPasta: function (ing1, ing2, ing3) {
        console.log(`Here is your delicious pasta with ${ing1},${ing2},${ing2}`);
    },

    orderPizza: function (mainIngredient, ...otherIngredients) {
        console.log(mainIngredient);
        console.log(otherIngredients);
    },
};
```

## 2.21. Desctructuring

### 2.21.1. Destructuring Arrays

```js
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
```

### 2.21.2. Desturcturing Objects

We can simply use the object's element as **left value** to destructuring the elements in the obejct.

```js
const { name, openingHours, categories } = restaurant;
console.log(name, openingHours, categories);
```

If we want the variable name different with the property name of object get the original property name and using `:` to separate the variable name

```js
const { name: restaurantName, openingHours: Hours, categories: tags } = restaurant;
console.log(restaurantName, Hours, tags);
```

**Default Value** if the property existed in object, the default value will be replaced by property value, otherwise like menu below, new variable will remain default value, if we didn't define default value, the new variable will remain undefined

```js
const { menu = [], starterMenu: starters = [] } = restaurant;
console.log(menu, starters);

// Mutating (改变) variales
let a = 111;
let b = 999;
// Mutating a and b with obj
const obj = { a: 23, b: 7, c: 14 };
// we need add a parenthseis
({ a, b } = obj);
console.log(a, b); // a = 23, b = 7
```

#### 2.21.2.1. Nested(内嵌) Object

Destructuring `openingHours` first to find the `fri` element, then destructuring `fri` object to get the `open` and `close` element, and finally reassign (or **rename**) as `o` and `c`

```js
const {
    fri: { open: o, close: c },
} = openingHours;
console.log(o, c);
```

#### 2.21.2.2. Use Object as parameter in object function

```js
restaurant.orderDelivery(order);

// restaurant.orderDelivery({
// 	time: "22:30",
// 	address: "Via del Sole, 21",
// 	mainIndex: 2,
// 	starterIndex: 2,
// });
restaurant.orderDelivery({ address: '"Via del Sole, 21"', starterIndex: 1 });
```
