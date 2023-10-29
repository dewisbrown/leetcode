/*
 * Design a stack that supports push, pop, top, 
 * and retrieving the minimum element in constant time.

 * Implement the MinStack class:

 * MinStack() initializes the stack object.
 * void push(int val) pushes the element val onto the stack.
 * void pop() removes the element on the top of the stack.
 * int top() gets the top element of the stack.
 * int getMin() retrieves the minimum element in the stack.
 * 
 * You must implement a solution with O(1) time complexity for each function.
 */

 // LeetCode155 -> MinStack class
public class LeetCode155 {
    private final int SIZE = 20;
    private int[] stack;
    private int top;
    private int min;

    public LeetCode155() {
        stack = new int[SIZE];
        top = -1;
        min = Integer.MIN_VALUE;
    }

    /*
     * When inserting a new minimum element, a different 
     * value is stored in the stack than the supplied value:
     * 1. Insert calulated number into stack
     *      stack[++top] = 2 * j - min
     * 2. update min:
     *      min = j;
     */
    public void push(int j) {
        if (isEmpty()) {
            min = j;
            stack[++top] = j;
        } else {
            if (j >= min) {
                stack[++top] = j;
            } else {
                stack[++top] = 2 * j - min;
                min = j;
            }
        }
    }
    
    /* A similar process is done when removing the 
     * minimum element:
     * 1. use a temp variable to hold min,
     * 2. update min:
     *      min = 2 * min - stack[top--];
     * 3. return temp variable
     */
    public int pop() {
        if (top() < min) {          // if top is less than minimum
            int temp = min;         // return min
            min = 2 * min - stack[top--];// update min value
            return temp;
        } else {
            return stack[top--];
        }
    }

    public int top() {
        return stack[top];
    }

    public int getMin() {
        return min;
    }

    public boolean isEmpty() {
        return top == -1;
    }
}