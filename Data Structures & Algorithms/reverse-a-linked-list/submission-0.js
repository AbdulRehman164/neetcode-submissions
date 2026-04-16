/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(head) {
        let cur = head;
        let vals = [];
        while (cur) {
            vals.push(cur.val);
            cur = cur.next;
        }
        cur = head;
        for (let i = vals.length - 1; i >= 0; i--) {
            cur.val = vals[i];
            cur = cur.next;
        }
        return head;
    }
}
