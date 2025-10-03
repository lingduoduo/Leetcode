class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

class Solution {
  oddEvenList(head: ListNode | null): ListNode | null {
    if (!head || !head.next) return head;

    // odd nodes: 1 -> 3 -> 5 ...
    // even nodes: 2 -> 4 -> 6 ...
    let odd: ListNode = head;
    let even: ListNode | null = head.next;
    const evenHead: ListNode = even; // keep start of even list

    while (even && even.next) {
      odd.next = even.next;     // link next odd
      odd = odd.next;           // advance odd
      even.next = odd.next;     // link next even
      even = even.next;         // advance even
    }

    odd.next = evenHead;        // append even list after odd list
    return head;
  }
}
