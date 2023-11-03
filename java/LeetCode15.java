import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

/**
 * Given an integer array nums, return all the triplets 
 * [nums[i], nums[j], nums[k]] such that 
 * i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
 * 
 * Notice that the solution set must not contain duplicate triplets.
 */
public class LeetCode15 {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        int n = nums.length;
        Arrays.sort(nums);

        for (int i = 0; i < n; i++) {
            // Handles duplicate values for 'a' (a + b + c = 0)
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            // Starting position of pointers
            int l = i + 1;
            int r = n - 1;
            
            while (l < r) {
                int threeSum = nums[i] + nums[l] + nums[r];
                if (threeSum > 0) {
                    r--;
                } else if (threeSum < 0) {
                    l++;
                } else {
                    List<Integer> list = new ArrayList<>(Arrays.asList(nums[i], nums[l], nums[r]));
                    res.add(list);

                    // update left pointer after adding threeSum list
                    l++;
                    while (nums[l] == nums[l - 1] && l < r) {
                        l++;
                    }
                }
            }
        }

        return res;
    }
}
