public static boolean isStringPalindrome(String str){
    if (str == null){
        return true;
    }
    
    if (str.isEmpty()){
        return true;
    }

    int totalOddCount = 0; // if more than one not palindrome 
    
    HashMap<Character,Integer> characterSet = new HashMap<Character,Integer>();
    Integer count = 0;

    for (char c : str.toCharArray()){ // mark frequencies of characters in that string 
        count = characterSet.containsKey(c) ? characterSet.get(c) : 0;
        characterSet.put(c, count + 1);
    }
    for (char c : str.toCharArray()){
        count = characterSet.containsKey(c) ? characterSet.get(c) : 0;
        
        if (count % 2 == 1){ // if the frequencies is odd number
            totalOddCount += 1;
        }
    }
    
    return totalOddCount <= 1;
}

/////// another way to solve it by converting to a char and checking in place:

public static boolean isStringPalindrome(String str){
    if (str == null){
        return true;
    }
    
    if (str.isEmpty()){
        return true;
    }

    char[] arr = str.toCharArray();
    
    for(int i =0; i < arr.length/2; i++){
        if(arr.length % 2 == 0) {// is even 0 1 2 3
            if (arr[i] != arr[(arr.length-1)-i]){
                return false;
            }
        }
        if(arr.length % 2 == 1) {// is odd say its 3 --> 0 1 2
            if (arr[i] != arr[(arr.length-1)-i]){
                return false;
            }
            if ((arr.length+1)/2 == i){
                break;
            }
        }
    }
    return true;
}

///// another way to recursively solve this
public static boolean isStringPalindrome(String str){
    if (str == null) return true;
    
    int len = str.length();
    if (len <= 1) return true;
    
    return str.charAt(0) == str.charAt(len - 1) &&
           isStringPalindrome(str.substring(1, len - 1));
}