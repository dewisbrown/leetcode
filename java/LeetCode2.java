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
        long num1 = 0;
        long num2 = 0;

        long i = 1;
        while (l1 != null) {
            long digit = i * l1.val;
            num1 += digit;
            l1 = l1.next;
            i *= 10;
        }

        i = 1;
        while (l2 != null) {
            long digit = i * l2.val;
            num2 += digit;
            l2 = l2.next;
            i *= 10;
        }

        long twoSum = num1 + num2;

        ListNode res = new ListNode((int)(twoSum % 10));
        ListNode curr = res;
        twoSum /= 10;

        while (twoSum > 0) {
            curr.next = new ListNode((int)(twoSum % 10));
            curr = curr.next;
            twoSum /= 10;
        }

        return res;
    }
}
