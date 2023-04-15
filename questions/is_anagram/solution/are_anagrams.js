// JavaScript Solution By Sophia (github/bunnydeviloper)
// to run in your terminal: `node <filename.js>`

const testA = "abcdefg"
const testB = "yummy #01"
const testC = "umymy #10"

// use array
const are_anagrams = (s1, s2) => {
  if (s1.length !== s2.length) return false;

  let tempS2 = s2.split(""); // create temporary array for string2

  // loop through S1, if current char in s1 matches any char in S2, then remove that from tempS2
  s1.split("").map(curr => {
    if (tempS2.includes(curr)) {
      tempS2 = tempS2.filter(e => e !== curr);
    }
  });

  // if all char matches, the length of temp array should be 0
  return tempS2.length === 0;
};

// time: O(n)
// space: O(n)

console.log(are_anagrams(testA, testB)); // false
console.log(are_anagrams(testB, testC)); // true

// use object
const are_anagrams2 = (s1, s2) => {
  if (s1.length !== s2.length) return false;

  let obj = {};

  // first loop through string1, add each character to object and increase its occurance number
  for (let i = 0; i < s1.length; i++ ) {
    if (!obj[s1.charAt(i)]) obj[s1.charAt(i)] = 1;
    else obj[s1.charAt(i)]++;
  }

  // second, loop through string2, check each character agains our obj, and reduce occurance number
  for (let i = 0; i < s2.length; i++) {
    if (!obj[s2.charAt(i)]) return false;
    else obj[s2.charAt(i)]--;
  }
  // finally, filter the object by any values that's not zero, there should be none
  return Object.values(obj).filter(e => e !== 0).length === 0;

};

console.log(are_anagrams2(testA, testB)); // false
console.log(are_anagrams2(testB, testC)); // true
