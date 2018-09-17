// JavaScript Solution By Sophia (github.com/bunnydeviloper)
// to run in your ternimal: `node <filename.js>`

function findLonelyNumber (a) {
  // create an object with keys as unique numbers in the array, and values are its occurances
  const myobj = a.reduce((obj, curr) => {
    if (!obj[curr]) obj[curr] = 1;
    else obj[curr]++;
    return obj;
  }, {})

  // return the key (unique number) that occurs only once (value === 1)
  return Object.keys(myobj).find(e => myobj[e] === 1);
}

console.log("[2, 6, 3, 8, 6, 2, 3]: ", findLonelyNumber([2, 6, 3, 8, 6, 2, 3])); // 8
console.log("[-1, -1, 0, 1, 1, 1]: ", findLonelyNumber([-1, -1, 0, 1, 1, 1])); // 0

// time: O(n)
// space: O(n)

// NOTE: using array.map() instead of array.reduce()
// let myobj = {};
// a.map(e => {
//   if (!myobj[e]) myobj[e] = 1;
//   else myobj[e]++;
// });
