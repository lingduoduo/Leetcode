// Definition for singly-linked list.
class ListNode{
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null){
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

class Solution{
  reverseBetween(head: ListNode | null, left: number, right: number): ListNode | null {
    if (!head || left === right) return head;

    const dummy = new ListNode(0, head);

    // Move `pre` to the node just before position `left`
    let pre: ListNode = dummy;
    for (let i = 1; i < left; i++) {
      pre = pre.next!;
    }

    // p0/p1/p2 reverse inside [left, right]
    let p0: ListNode | null = null;       // prev within the sublist
    let p1: ListNode | null = pre.next;   // current within the sublist
    let p2: ListNode | null = null;       // next within the sublist

    for (let i = 0; i < right - left + 1 && p1; i++) {
      p2 = p1.next;
      p1.next = p0;
      p0 = p1;
      p1 = p2;
    }

    // Reconnect:
    // pre.next was the original left node; it's now the tail of the reversed segment
    const leftNode = pre.next!;
    pre.next = p0;        // new head of reversed block
    leftNode.next = p1;   // connect tail of reversed block to the remainder

    return dummy.next;
  }
}
