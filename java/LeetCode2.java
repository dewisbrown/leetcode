/**
 * You are given two non-empty linked lists representing two 
 * non-negative integers. The digits are stored in reverse order, 
 * and each of their nodes contains a single digit. 
 * Add the two numbers and return the sum as a linked list.
 * 
 * You may assume the two numbers do not contain any leading zero, 
 * except the number 0 itself.
 */
public class LeetCode2 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // set first node value
        int sum = l1.val + l2.val;
        int remainder = (sum / 10 > 0) ? 1 : 0;
        ListNode res;

        if (remainder == 0) {
            res = new ListNode(sum);
        } else {
            res = new ListNode(sum % 10);
        }

        ListNode curr = res;
        l1 = l1.next;
        l2 = l2.next;

        // iterate through lists until one is null
        while (l1 != null && l2 != null) {
            sum = l1.val + l2.val + remainder;
            
            // check if sum is two digits
            remainder = (sum / 10 > 0) ? 1 : 0;

            if (remainder == 0) {
                curr.next = new ListNode(sum);
            } else {
                curr.next = new ListNode(sum % 10);
            }

            // move pointers
            l1 = l1.next;
            l2 = l2.next;
            curr = curr.next;
        }

        // check if either list still has values
        while (l1 != null) {
            sum = l1.val + remainder;
            remainder = (sum / 10 > 0) ? 1 : 0;

            if (remainder == 0) {
                curr.next = new ListNode(sum);
            } else {
                curr.next = new ListNode(sum % 10);
            }

            curr = curr.next;
            l1 = l1.next;
        }
        
        while (l2 != null) {
            sum = l2.val + remainder;
            remainder = (sum / 10 > 0) ? 1 : 0;

            if (remainder == 0) {
                curr.next = new ListNode(sum);
            } else {
                curr.next = new ListNode(sum % 10);
            }

            curr = curr.next;
            l2 = l2.next;
        }

        // if there is still a remainder, add one more node with val = 1
        if (remainder > 0) {
            curr.next = new ListNode(1);
        }

        return res;
    }
}
