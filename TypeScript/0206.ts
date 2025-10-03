
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
  reverseList(head: ListNode | null): ListNode | null {
    let p0: ListNode | null = null;      // prev
    let p1: ListNode | null = head;      // curr

    while (p1) {
      let p2: ListNode | null = p1.next; // next
      p1.next = p0;                       // reverse link
      p0 = p1;                            // advance prev
      p1 = p2;                            // advance curr
    }
    return p0; // new head
  }
}