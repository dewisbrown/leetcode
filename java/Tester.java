/**
 * Class with main method to test solutions.
 */
public class Tester {
    
    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);
        
        LeetCode143 test = new LeetCode143();

        ListNode curr = head;

        System.out.println("Before reorder:");
        while (curr != null) {
            System.out.print("[" + curr.val + "] -> ");
            curr = curr.next;
        }
        System.out.println();

        test.reorderList(head);

        curr = head;

        System.out.println("After reorder:");
        while (curr != null) {
            System.out.print("[" + curr.val + "] -> ");
            curr = curr.next;
        }
        System.out.println();
    }
}
