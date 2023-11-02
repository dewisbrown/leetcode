import java.util.Stack;

/**
 * Given an array of integers heights representing the histogram's bar 
 * height where the width of each bar is 1, 
 * return the area of the largest rectangle in the histogram.
 */
class LeetCode84 {
    public int largestRectangleArea(int[] heights) {
        Stack<int[]> stack = new Stack<>();
        int n = heights.length;
        int maxArea = 0;

        for (int i = 0; i < n; i++) {
            int start = i;

            while (!stack.isEmpty() && stack.peek()[1] > heights[i]) {
                int[] pair = stack.pop();
                maxArea = Math.max(maxArea, pair[1] * (i - pair[0]));
                start = pair[0];
            }

            stack.push(new int[]{start, heights[i]});
        }

        while (!stack.isEmpty()) {
            int[] pair = stack.pop();
            maxArea = Math.max(maxArea, pair[1] * (n - pair[0]));
        }

        return maxArea;
    }
}
