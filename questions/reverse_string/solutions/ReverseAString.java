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
// recursively:

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
