/**
 * Given head, the head of a linked list, determine if the linked list 
 * has a cycle in it.
 * 
 * There is a cycle in a linked list if there is some node 
 * in the list that can be reached again by continuously 
 * following the next pointer. Internally, pos is used to denote t
 * he index of the node that tail's next pointer is connected to. 
 * Note that pos is not passed as a parameter.
 * 
 * Return true if there is a cycle in the linked list. 
 * Otherwise, return false.
 */
public class LeetCode141 {
    public boolean hasCycle(ListNode head) {
        // Floyd's Cycle-Finding Algorithm
        // uses O(1) space and O(n) time
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            
            if (slow == fast)
                return true;
        }
        return false;
    }
}
