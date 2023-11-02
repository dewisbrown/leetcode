import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Stack;

/**
 * There are n cars going to the same destination along a one-lane road. 
 * The destination is target miles away.
 * You are given two integer array position and speed, 
 * both of length n, where position[i] is the position of the ith car 
 * and speed[i] is the speed of the ith car (in miles per hour).
 * A car can never pass another car ahead of it, but it can catch up 
 * to it and drive bumper to bumper at the same speed. The faster car will 
 * slow down to match the slower car's speed. 
 * The distance between these two cars is ignored 
 * (i.e., they are assumed to have the same position).
 * A car fleet is some non-empty set of cars driving at the same position and same speed. 
 * Note that a single car is also a car fleet.
 * If a car catches up to a car fleet right at the destination point, 
 * it will still be considered as one car fleet.
 * 
 * Return the number of car fleets that will arrive at the destination.
 */
public class LeetCode853 {
    public int carFleet(int target, int[] position, int[] speed) {
        Stack<Double> stack = new Stack<>();
        int n = position.length;
        
        // Create pairs
        List<Pair> pairs = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            pairs.add(new Pair(position[i], speed[i]));
        }

        // Sort pairs
        pairs.sort(Comparator.comparing(Pair::getA));

        // Loop through sorted pair list
        for (int i = n - 1; i >= 0; i--) {
            double oldTop = -1;
            if (!stack.isEmpty()) {
                oldTop = stack.peek();
            }

            stack.push((double)(target - pairs.get(i).a) / pairs.get(i).b);
            
            // compare top of stack with 2nd stack element
            if (stack.size() >= 2 && stack.peek() <= oldTop) {
                stack.pop();
            }
        }
        return stack.size();
    }
}

class Pair {
    int a;
    int b;

    public Pair(int a, int b) {
        this.a = a;
        this.b = b;
    }

    public int getA() {
        return a;
    }

    public int getB() {
        return b;
    }

    @Override
    public String toString() {
        return String.format("(%d, %d)", a, b);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Pair pair = (Pair) o;
        return pair.a == a && pair.b == b;
    }

    @Override
    public int hashCode() {
        return Integer.hashCode(a) * 31 + Integer.hashCode(b);
    }
}

