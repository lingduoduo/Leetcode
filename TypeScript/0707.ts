class ListNode {
  public val: number;
  public next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

class MyLinkedList {
  private size: number;
  private head: ListNode | null;
  private tail: ListNode | null;

  constructor() {
    this.size = 0;
    this.head = null;
    this.tail = null;
  }

  // returns node at index (0-based). Caller must ensure 0 <= index < size.
  private getNode(index: number): ListNode {
    let cur = this.head as ListNode; // safe because caller checks bounds
    for (let i = 0; i < index; i++) {
      cur = cur.next as ListNode; // safe due to bounds
    }
    return cur;
  }

  get(index: number): number {
    if (index < 0 || index >= this.size) return -1;
    return this.getNode(index).val;
  }

  addAtHead(val: number): void {
    const node = new ListNode(val, this.head);
    this.head = node;
    if (this.size === 0) this.tail = node;
    this.size++;
  }

  addAtTail(val: number): void {
    const node = new ListNode(val, null);
    if (this.size === 0) {
      this.head = node;
      this.tail = node;
    } else {
      (this.tail as ListNode).next = node;
      this.tail = node;
    }
    this.size++;
  }

  addAtIndex(index: number, val: number): void {
    if (index > this.size) return;       // invalid (beyond tail)
    if (index <= 0) { this.addAtHead(val); return; }   // insert at head
    if (index === this.size) { this.addAtTail(val); return; } // insert at tail

    const prev = this.getNode(index - 1);
    const node = new ListNode(val, prev.next);
    prev.next = node;
    this.size++;
  }

  deleteAtIndex(index: number): void {
    if (index < 0 || index >= this.size) return;

    if (index === 0) {
      this.head = this.head!.next;
      this.size--;
      if (this.size === 0) this.tail = null; // list became empty
      return;
    }

    const prev = this.getNode(index - 1);
    const toDelete = prev.next as ListNode;
    prev.next = toDelete.next;

    if (index === this.size - 1) {
      // deleted the tail
      this.tail = prev;
    }
    this.size--;
  }
}

// --- quick sanity checks ---
const ll = new MyLinkedList();
ll.addAtHead(1);           // [1]
ll.addAtTail(3);           // [1,3]
ll.addAtIndex(1, 2);       // [1,2,3]
console.log(ll.get(1));    // 2
ll.deleteAtIndex(1);       // [1,3]
console.log(ll.get(1));    // 3
ll.deleteAtIndex(1);       // [1]
ll.deleteAtIndex(0);       // []
console.log(ll.get(0));    // -1
