import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int a[] = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }

    int value = 0;

    for (int i : a) {
        value ^= i; // preform XOR
    }
    System.out.println(value);
}

/* Can also solve this problem with a hastable*/

//         // base case
//         if (n == 1){
//             System.out.println(n);
//             return;
//         }
        
//         Integer count = 0;
//         Hashtable<Integer, Integer> ht = new Hashtable<>();
        
//         for(Integer i : a){
//             count = ht.containsKey(i) ? ht.get(i) : 0;
//             ht.put(i,count+1);
//         }
        
//          for(Integer i : a){
//               count = ht.get(i);
                  
//                 if(count == 1){
//                       System.out.println(i);
//                 }
//          }
//     }
}
