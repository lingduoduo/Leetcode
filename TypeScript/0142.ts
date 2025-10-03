// Definition for singly-linked list.
class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

class Solution {
  detectCycle(head: ListNode | null): ListNode | null {
    let slow: ListNode | null = head;
    let fast: ListNode | null = head;

    // Phase 1: find meeting point (if any)
    while (fast && fast.next) {
      slow = slow!.next;            // safe due to loop condition
      fast = fast.next.next;        // may become null at tail
      if (slow === fast) {          // cycle detected
        // Phase 2: move one pointer to head; step both to find entry
        slow = head;
        while (slow !== fast) {
          slow = slow!.next;
          fast = fast!.next;
        }
        return slow;                // cycle entry
      }
    }
    return null;                    // no cycle
  }
}
