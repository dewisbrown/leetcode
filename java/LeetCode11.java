/**
 * You are given an integer array height of length n. 
 * There are n vertical lines drawn such that 
 * the two endpoints of the ith line are (i, 0) and (i, height[i]).
 * 
 * Find two lines that together with the x-axis form a container, 
 * such that the container contains the most water.
 * 
 * Return the maximum amount of water a container can store.
 * Notice that you may not slant the container.
 */
public class LeetCode11 {
    public int maxArea(int[] height) {
        int n = height.length;
        int maxArea = 0;
        int l = 0;
        int r = n - 1;
        
        /* 
         * left pointer at index 0, right pointer at n - 1
         * 1. find area
         * 2. compare to maxArea and update if larger
         * 3a. increment left pointer if height[l] < height[r]
         * 3b. decrement right pointer if height[r] < height[l]
         */ 
 
        while (l < r) {
            int area = Math.min(height[l], height[r]) * (r - l);
            maxArea = Math.max(area, maxArea);
            
            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }
        return maxArea;
    }
}
