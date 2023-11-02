import java.util.Stack;

/**
 * Given an array of integers temperatures represents 
 * the daily temperatures, return an array answer such 
 * that answer[i] is the number of days you have to wait 
 * after the ith day to get a warmer temperature. 
 * 
 * If there is no future day for which this is possible, 
 * keep answer[i] == 0 instead.
 */
public class LeetCode739 {
    
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        Stack<Integer> stack = new Stack<>();
        int[] ans = new int[n];

        for (int i = n - 1; i >= 0; i--) {

            while (!stack.isEmpty() && temperatures[i] >= temperatures[stack.peek()]) {
                stack.pop();
            }

            if (!stack.isEmpty()) {
                ans[i] = stack.peek() - i;
            }

            stack.push(i);
        }
        
        for (int i = n - 1; i >= 0; i--) {
            // Pop indices until a higher value is found
            while (!stack.isEmpty() && temperatures[i] >= temperatures[stack.peek()]) {
                stack.pop();
            }
            
            // The index of the higher value is at top of stack now
            if (!stack.isEmpty()) {
                ans[i] = stack.peek() - i;
            }

            stack.push(i);
        }
        
        return ans;
    }
}
