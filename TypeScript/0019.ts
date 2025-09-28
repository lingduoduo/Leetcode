// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

class Solution {
  removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    const dummy = new ListNode(0, head);
    let fast: ListNode | null = dummy;
    let slow: ListNode | null = dummy;

    // move fast n steps ahead
    for (let i = 0; i < n; i++) {
      if (!fast) return head; // defensive; shouldn't happen with valid n
      fast = fast.next;
    }

    // move both until fast is at tail
    while (fast && fast.next) {
      fast = fast.next;
      slow = slow!.next;
    }

    slow.next = slow.next.next;
    return dummy.next;
  }
}