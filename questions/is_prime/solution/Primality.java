public class Solution {
    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        
        for (int i=0; i<t; i++)  {
            int n = scan.nextInt();
            System.out.println(isPrime(n) ? "Prime" : "Not prime");
        }
    }
    
    public static boolean isPrime(int n) {
        
        if (n < 2) {
            return false;
        } else if (n == 2) {
            return true;
        } else if (n % 2 == 0) {
            return false;
        }

        int sqrt = (int) Math.sqrt(n);
        
        for (int i = 2; i <= sqrt; i ++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}