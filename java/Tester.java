import java.util.ArrayList;
import java.util.List;

/**
 * Class with main method to test solutions.
 */
public class Tester {
    
    public static void main(String[] args) {
        List<int[]> list = new ArrayList<>();
        list.add(new int[]{1, 8, 6, 2, 5, 4, 8, 3, 7});
        list.add(new int[]{1, 1});

        LeetCode11 test = new LeetCode11();

        for (int[] height : list) {
            System.out.println(test.maxArea(height));
        }
    }
}
