/*
 * Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 * 
 * Example:
 * Input: n = 3
 * Output: ["((()))","(()())","(())()","()(())","()()()"]
 */

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.stream.Collectors;

public class LeetCode22 {
    List<String> ans = new ArrayList<>();
    Stack<String> stack = new Stack<>();

    public List<String> generateParentheses(int n) {
        backtrack(n, 0, 0);
        return ans;
    }

    /**
     * Add contents of stack when open and closed parentheses counts 
     * are equal to n.
     *
     * Conditions for adding parentheses:
     * Add open parentheses if open count is less than n.
     * Add closed parentheses if closed count is less than open count.
     * 
     * Backtrack by popping the character after the recursive call.
     */
    public void backtrack(int n, int open, int closed) {
        // Base case
        if (open == n && closed == n) {
            ans.add(stack.stream().map(s -> s.toString()).collect(Collectors.joining("")));
            return;
        }

        if (open < n) {
            stack.push("(");
            backtrack(n, open + 1, closed);
            stack.pop();
        }

        if (closed < open) {
            stack.push(")");
            backtrack(n, open, closed + 1);
            stack.pop();
        }
    }
}
