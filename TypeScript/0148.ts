function sortList(head: ListNode | null): ListNode | null {
    if (head === null || head.next === null) return head;

    // find middle (slow/fast pointers)
    let slow: ListNode = head;
    let fast: ListNode | null = head;

    while (fast !== null && fast.next !== null && fast.next.next !== null) {
        slow = slow.next as ListNode;
        fast = fast.next.next;
    }

    // split into two halves
    let half: ListNode | null = slow.next;
    slow.next = null;

    const left = sortList(head);
    const right = sortList(half);

    return merge(left, right);
}

function merge(left: ListNode | null, right: ListNode | null): ListNode | null {
    const dummy = new ListNode();
    let p = dummy;

    while (left !== null && right !== null) {
        if (left.val < right.val) {
            p.next = left;
            left = left.next;
        } else {
            p.next = right;
            right = right.next;
        }
        p = p.next;
    }

    p.next = left !== null ? left : right;
    return dummy.next;
}
