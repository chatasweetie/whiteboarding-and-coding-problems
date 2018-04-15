// time complexity = o(n) where n is the length of the string
// space is constant

public static String reverseString(String str){
    
    if (str.isEmpty()){
        return str;
    }else if (str == null){
        return null;
    }
    
    char[] c = str.toCharArray();

    for (int i = 0 ; i < c.length/2; i++){ // **  swap in array **
        char temp = c[i];
        c[i] = c[c.length - i];
        c[c.length - i] = temp;
     }
    
    //  String output = new String(c);
    //  return output;
    return new String(c);
}






// ========================================
// You can put a spin on your 'reverse a string' coding question - 
// first have them write a func that prints out a C string without 
// looping constructs or using local vars. Then if they get that, 
// ask them to implement a reverse string function in the same manner 
// as the first one. Don't say "use recursion" - let them figure out 
// its straightforward applicability to the problem. That's, IMHO, how 
// you can gauge if they 'think recursively' when lightly nudged in that 
// direction:

void print(char *s) {
  if (*s != 0) {
    putchar(*s);
    print(s+1);
  }
}

void printreverse(char *s) {
  if (*s != 0)
    printreverse(s+1);
    putchar(*s);
  }
}

int main() {
  char *s = "Hello world";
  print(s);
  putchar('\n');
  printreverse(s);
  putchar('\n');
}