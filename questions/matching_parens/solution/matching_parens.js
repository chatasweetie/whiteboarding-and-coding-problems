// JavaScript Solution By Sophia (github.com/bunnydeviloper)
// run in your terminal by: `node <filename.js>`

// Simple version: the string only has one type of bracket "(", ")"
function matchingParen(s) {
  let parentheses = 0;

  // use for loop or while loop to check each character of the string
  for (let i = 0; i < s.length; i ++) {
    if (s.charAt(i) === "(") parentheses++;
    if (s.charAt(i) === ")") parentheses--;
    if (parentheses < 0) return false; // if the starting char is a closing bracket, return false
  }

  return parentheses === 0; // same as return (parentheses === 0) ? true : false;
}

// time: O(n)
// space: O(1)

console.log(")I lov(e): ", matchingParen(")I lov(e)")); // False
console.log("(Hello(): ", matchingParen("(Hello()")); // False
console.log("Hi(): ", matchingParen("Hi()")); // True

// ---------------
// Complex version: the string has a mixed of multiple types of brackets
// initialize the pairs in the parameter so users can personalize their brackets type
// (eg: {"<":">", "`":"`"})
function moreParentheses(s, pairs = {"(":")", "[":"]", "{":"}"}) {
  let stack = [];

  // loop through the string
  for (let i = 0; i < s.length; i++) {
    // if the current character is an open bracket, push it on to the stack
    if (Object.keys(pairs).includes(s.charAt(i))) {
      stack.push(s.charAt(i));
    }

    // if the current character is a closing bracket
    if (Object.values(pairs).includes(s.charAt(i))) {
      // and this closing bracket matches with the last open bracket in our stack, then pop stack
      let keyToCompare = Object.keys(pairs).find(k => pairs[k] === s.charAt(i));
      if (stack[stack.length - 1] === keyToCompare) stack.pop();
      // otherwise, return false
      else return false;
    }
  }
  return stack.length === 0;
}

// time: O(n)
// space: O(n/2)

console.log("[hello()]{}: ", moreParentheses("[hello()]{}")); // True
console.log("]hello()]{}: ", moreParentheses("]hello()]{}")); // False
console.log("[(]{)}: ", moreParentheses("[(]{)}")); // False
