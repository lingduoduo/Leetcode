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
  getIntersectionNode(headA: ListNode | null, headB: ListNode | null): ListNode | null {
    // Two-pointer technique: walk each list; when hitting null, jump to the other head.
    // If there is an intersection by reference, pointers meet there; otherwise both hit null.
    let pa: ListNode | null = headA;
    let pb: ListNode | null = headB;
    while (pa !== pb) {
      pa = pa ? pa.next : headB;
      pb = pb ? pb.next : headA;
    }
    return pa; // either the intersection node or null
  }
}

