/**
 * You are given the head of a singly linked-list. 
 * The list can be represented as:
 * L0 → L1 → … → Ln - 1 → Ln
 * 
 * Reorder the list to be on the following form:
 * L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
 * 
 * You may not modify the values in the list's nodes. 
 * Only nodes themselves may be changed.
 */
public class LeetCode143 {
    public LeetCode143() {}
    public void reorderList(ListNode head) {
        ListNode fast = head.next;
        ListNode slow = head;

        // use fast and slow pointer to find middle of linked list
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        ListNode second = slow.next;    // starting node of second half of list
        slow.next = null;               // remove link to second half

        ListNode prev = null;
        while (second != null) {        // reverse second half
            ListNode temp = second.next;
            second.next = prev;
            prev = second;
            second = temp;
        }
        second = prev;

        ListNode first = head;
        while (second != null) {        // merge two halves
            ListNode temp1 = first.next;
            ListNode temp2 = second.next;

            first.next = second;
            second.next = temp1;

            // move pointers
            second = temp2;
            first = temp1;
        }
    }

    public void reverseList(ListNode node) {
        ListNode prev = new ListNode();
        ListNode curr = node;
        ListNode next = new ListNode();

        while (curr != null) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        node = prev;
    }
}
