// JavaScript Solution By Sophia (github.com/bunnydeviloper)
// to test in your terminal: `node <filename.js>`

function searchBST(value, node) {
  if (!node) return false;
  else if (node.value > value) return searchBST(value, node.left);
  else if (node.value < value) return searchBST(value, node.right);
  else return true; // this is when node.value === value
}

// -------------------------------------
// constructor function for BST and Node
function BST () {
  this.root = null;
}
function Node(value, left = null, right = null) {
  this.value = value;
  this.left = left;
  this.right = right;
}
// function for inserting a new value into the BST
BST.prototype.insert = function(value) {
  const newNode = new Node(value);
  if (!this.root) return this.root = newNode;

  let current = this.root;
  while (current) {
    if (current.value === value) {
      break; // duplicate value, just ignore, no need to insert newNode
    } else if (current.value > value) {
      if (!current.left) {
        current.left = newNode;
        break; // insert newNode and break out of while loop
      } else {
        current = current.left; // keep on traversing down
      }
    } else {
      if (!current.right) {
        current.right = newNode;
        break; // insert newNode and break out of while loop
      } else {
        current = current.right; // keep on traversing down
      }
    }
  }
};

const mybst = new BST();
mybst.insert(20);
mybst.insert(9);
mybst.insert(25);
mybst.insert(15);
mybst.insert(5);
mybst.insert(22);
mybst.insert(12);
mybst.insert(8);
mybst.insert(23);
// console.dir(mybst, {depth: null});

// ------------------- test ----------------------
console.log(searchBST(0, mybst.root)); // false
console.log(searchBST(15, mybst.root)); // true
