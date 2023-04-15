// JavaScript Solution by Sophia (github.com/bunnydeviloper)
// to run in your terminal: `node <filename.js>`

// INSTRUCTION: same as matchingParen exercise, but use recursion
function validParentheses(s, pairs = {"(":")", "[":"]", "{":"}"}, stack = []) {
  if (!s) return stack.length === 0; // base case

  // if the first char of the current string is an open bracket, push it on to the stack
  if (Object.keys(pairs).includes(s.charAt(0))) {
    stack.push(s.charAt(0));
  }
  // if the first char of the current string is a closing bracket
  if (Object.values(pairs).includes(s.charAt(0))) {
    // and this closing bracket matches with the last begining bracket in our stack, then pop stack
    let keyToCompare = Object.keys(pairs).find(k => pairs[k] === s.charAt(0));
    if (stack[stack.length - 1] === keyToCompare) stack.pop();
    // otherwise, return false
    else return false;
  }

  // each recursive call, we remove the first character of the original string
  return validParentheses(s.substring(1), pairs, stack);
}

// time: O(n)
// space: O(n)

console.log("(x)[y](z) ([hello](world)[]): ", validParentheses("(x)[y](z) ([hello](world)[])")); // True
console.log("( (] ([)]: ", validParentheses("( (] ([)]")); // False
console.log("({foo)}: ", validParentheses("({foo)}")); // False
