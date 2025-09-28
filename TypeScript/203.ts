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
    removeElements(head: ListNode | null, val: number): ListNode | null {
    const dummy = new ListNode(0, head);
    let p: ListNode = dummy;

    while (p.next) {
      if (p.next.val === val) {
        p.next = p.next.next; // skip the node
      } else {
        p = p.next;           // move forward
      }
    }
    return dummy.next;
  }
}