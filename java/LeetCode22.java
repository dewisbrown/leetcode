/*
 * Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 * 
 * Example:
 * Input: n = 3
 * Output: ["((()))","(()())","(())()","()(())","()()()"]
 */

import java.util.ArrayList;
import java.util.List;

public class LeetCode22 {
    List<String> ans = new ArrayList<>();
    public List<String> generateParenthesis(int n) {
        helper("(", n);
        return ans;
    }

    public void helper(String s, int n) {
        // Base case
        if (n == 0) {
            ans.add(s);
            return;
        }

        char c = s.charAt(s.length() - 1);

        if (c == '(') {
            s.concat(")");
            helper(s, n - 1);
        }

        if (c == ')') {
            
        }

    }
}
