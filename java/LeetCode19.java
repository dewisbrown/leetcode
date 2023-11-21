import java.util.HashMap;
import java.util.Map;

/**
 * Given the head of a linked list, remove the nth node from the end of the list and return its head.
 */
public class LeetCode19 {
    // my submission using extra space (map)
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head.next == null) return new ListNode();

        Map<Integer, ListNode> map = new HashMap<>();
        ListNode curr = head;

        // find count of linked list
        int count = 0;
        while (curr != null) {
            map.put(count, curr);
            curr = curr.next;
            count++;
        }

        // check if removing first node
        if (count == n) {
            return head.next;
        }

        ListNode remove = map.get(count - n);
        ListNode prev = map.get(count - n - 1);
        
        if (remove.next == null) {
            prev.next = null;
        } else {
            prev.next = remove.next;
        }

        return head;
    }

    // two pointer method, faster and doesn't use extra memory (map)
    public ListNode removeNthFromEnd2(ListNode head, int n) {
        ListNode fast = head, slow = head;
        
        for (int i = 0; i < n; i++) {
            fast = fast.next;
        }

        if (fast == null) return head.next; // linked list count == n

        while (fast.next != null) {
            fast = fast.next;
            slow = slow.next;
        }
        slow.next = slow.next.next;
        return head;
    }
}
