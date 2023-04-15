// JavaScript Solution By Sophia (github.com/bunnydeviloper)
// To test in your terminal: `node <filename.js`

// Decoding Morse Code
function translate(array, tree) {
  let message = "";
  if (array.length === 0) return "There's no current message.";

  // loop through each element of the array and find out the corresponding character
  array.map(letter => {
    let current = tree.root;
    for (let i=0; i < letter.length; i++) {
      if (letter.charAt(i) === "." && current.left) current = current.left;
      if (letter.charAt(i) === "-" && current.right) current = current.right;
    }
    message += current.value;
  });
  return message;
}

// time: O(2n) => O(n), note: time for inner for loop is O(5) b/c max depth of morse code tree is 5 levels
// space: O(n)

// -------------------------------------
// Constructor functions for Tree and Nodes
function Tree () {
  this.root = null;
}
function Node(value, left = null, right = null) {
  this.value = value;
  this.left = left;
  this.right = right;
}

// Morse Code Tree, left branch of the tree
const H = new Node("H", new Node(5), new Node(4));
const V = new Node("V", null, new Node(3));
const S = new Node("S", H, V);
const U = new Node("U", new Node("F"), new Node(null, null, new Node(2)));
const I = new Node("I", S, U);

const R = new Node("R", new Node("L"), new Node(null, new Node("+")))
const W = new Node("W", new Node("P"), new Node("J", null, new Node(1)));
const A = new Node("A", R, W);
const E = new Node("E", I, A);

// Morse Code Tree, right branch of the tree
const G = new Node("G", new Node("Z", new Node(7)), new Node("Q"));
const O = new Node("O", new Node(null, new Node(8)), new Node(null, new Node(9), new Node(0)));
const M = new Node("M", G, O);
const D = new Node("D", new Node("B", new Node(6), new Node("=")), new Node("X", new Node("/")));
const K = new Node("K", new Node("C"), new Node("Y"));
const N = new Node("N", D, K);
const T = new Node("T", N, M);

// putting left branch and right branch together
const morseCode = new Tree();
morseCode.root = new Node("start", E, T);
// console.dir(morseCode, {depth: null});

// -------------------------------------
// Test
console.log(translate(["....", ".", ".-..", ".-..", "---"], morseCode)); // HELLO
console.log(translate([], morseCode)); // There's no current message
console.log(translate(["..---", ".-.-.", "--...", "-...-", "----."], morseCode)); // 2 + 7 = 9
console.log(translate([".-..", ".-....", ".-..--"], morseCode)); // L, left of L: null -> return L, right of L: null -> return L
