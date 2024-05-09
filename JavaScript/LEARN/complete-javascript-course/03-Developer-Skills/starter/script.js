// Remember, we're gonna use strict mode in all scripts now!
'use strict';

/* const temperatures1 = [3, -2, -6, -1, "error", 9, 13, 17, 15, 14, 9, 5];
const temperatures2 = [3, -2, -6, -1, "error", 9, 13, 17, 15, 14, 9, 5];
const temperature = temperatures1.concat(temperatures2);
const calcAmplitude = function (temp1, temp2) {
    if (typeof temp1 !== "object" || typeof temp2 !== "object") return;
    const temp = temp1.concat(temp2);
    // console.log(temp);
    let highestTemp = temp[0];
    let lowestTemp = temp[0];
    for (let i = 1; i < temp.length; i++) {
        if (typeof temp[i] !== "number") continue;
        if (highestTemp < temp[i]) highestTemp = temp[i];
        if (lowestTemp > temp[i]) lowestTemp = temp[i];
    }
    return highestTemp - lowestTemp;
};

console.log(
    `the amplitude of temperature data array is ${calcAmplitude(
        temperatures1,
        temperatures2
    )}`
); */

// debug
/* const measurementKelvin = function () {
    const measurement = {
        type: "temp",
        unit: "celsius",
        // C) Fix
        // value: +prompt("Degrees celsius:"),
        value: 10,
        // value: Number(prompt("Degrees celsius:")),
    };
    // B) FIND
    console.table(measurement);
    const kelvin = measurement.value + 273;
    return kelvin;
};

// A) Identify
console.log(measurementKelvin());

const temperatures1 = [3, -2, -6, -1, "error", 9, 13, 17, 15, 14, 9, 5];
const temperatures2 = [3, -2, -6, -1, "error", 9, 13, 17, 15, 14, 9, 5];

const calcAmplitudeBug = function (temp1, temp2) {
    if (typeof temp1 !== "object" || typeof temp2 !== "object") return;
    const temp = temp1.concat(temp2);
    // console.log(temp);
    let highestTemp = temp[0];
    let lowestTemp = temp[0];
    for (let i = 1; i < temp.length; i++) {
        if (typeof temp[i] !== "number") continue;
        if (highestTemp < temp[i]) highestTemp = temp[i];
        if (lowestTemp > temp[i]) lowestTemp = temp[i];
    }
    return highestTemp - lowestTemp;
};

console.log(
    `the amplitude of temperature data array is ${calcAmplitudeBug(
        temperatures1,
        temperatures2
    )}`
); */

// Code Challenge #1
function printForecast(arr) {
    if (typeof arr !== 'object') return;
    let str = '';
    for (let i = 0; i < arr.length; i++) {
        str += `... ${arr[i]}°C in ${i + 1} days`;
    }
    str += '...';
    console.log(str);
}
const data1 = [17, 21, 23];
const data2 = [12, 5, -5, 0, 4];
printForecast(data1);
printForecast(data2);
