import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import org.apache.commons.lang.ArrayUtils;

public class Solution {
    
    public static boolean isBalanced(String expression) {
    Stack<Character> brackets = new Stack<Character>();

    for(int i=0; i<expression.length(); i++){
        char next = expression.charAt(i);
        if(next == '{')      brackets.push('}');
        else if(next == '[') brackets.push(']');
        else if(next == '(') brackets.push(')');
        else if(brackets.empty() || brackets.pop() != next) {
            return false;
        } 
    }
    return brackets.empty();
    }
  
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for (int a0 = 0; a0 < t; a0++) {
            String expression = in.next();
            System.out.println( (isBalanced(expression)) ? "YES" : "NO" );
        }
    }
}
