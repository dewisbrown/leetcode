/**
 * Class with main method to test solutions.
 */
public class Tester {
    
    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        ListNode curr = head;

        for (int i = 2; i < 6; i++) {
            curr.next = new ListNode(i);
            curr = curr.next;
        }

        while (head != null) {
            System.out.printf("[%d] -> ", head.val);
            head = head.next;
        }
    }
}
