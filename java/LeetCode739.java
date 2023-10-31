import java.util.HashMap;
import java.util.Map;

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
        int[] ans = new int[n];
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            if (map.containsKey(temperatures[i]) && i < map.get(temperatures[i])) {
                ans[i] = map.get(temperatures[i]) - i;
                continue;
            }
            for (int j = i + 1; j < n; j++) {
                if (temperatures[i] < temperatures[j]) {
                    map.put(temperatures[i], j);
                    ans[i] = j - i;
                    break;
                }
            }
        }
        
        return ans;
    }
}
