
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
  swapPairs(head: ListNode | null): ListNode | null {
    const dummy = new ListNode(0, head);
    let p0: ListNode = dummy;

    while (p0.next && p0.next.next) {
      const p1 = p0.next!;       // first node of the pair
      const p2 = p1.next!;       // second node of the pair

      // rewire pointers: p0 -> p2 -> p1 -> next
      p0.next = p2;
      p1.next = p2.next;
      p2.next = p1;

      // advance p0 to the end of the swapped pair
      p0 = p1;
    }
    return dummy.next;
  }
}
