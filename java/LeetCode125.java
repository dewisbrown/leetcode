/**
 * A phrase is a palindrome if, after converting all uppercase letters 
 * into lowercase letters and removing all non-alphanumeric characters, 
 * it reads the same forward and backward. 
 * Alphanumeric characters include letters and numbers.
 * 
 * Given a string s, return true if it is a palindrome, or false otherwise.
 */
public class LeetCode125 {
    public boolean isPalindrome(String s) {
        String str = s.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");
        
        if (str.isEmpty()) return true;
        
        int i = 0;
        int j = str.length() - 1;

        while (i < j) {
            if (str.charAt(i) != str.charAt(j))
                return false;
            i++;
            j--;
        }

        return true;
    }
}
