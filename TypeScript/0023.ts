// npm i @datastructures-js/priority-queue
import { MinPriorityQueue } from "@datastructures-js/priority-queue";

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
  // ✅ pass a function (t) => number, not { priority: ... }
  const pq = new MinPriorityQueue<[number, number, ListNode]>((t) => t[0]);

  for (let i = 0; i < lists.length; i++) {
    if (lists[i]) pq.enqueue([lists[i]!.val, i, lists[i]!]);
  }

  const dummy = new ListNode(0);
  let tail = dummy;

  while (!pq.isEmpty()) {
    // ✅ dequeue returns the tuple directly (no .element)
    const [, i, node] = pq.dequeue()!;
    tail.next = node;
    tail = node;
    if (node.next) pq.enqueue([node.next.val, i, node.next]);
  }

  return dummy.next;
}
