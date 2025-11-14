function insert(head: _Node | null, insertVal: number): _Node | null {
    if (!head) {
        const newNode = new _Node(insertVal);
        newNode.next = newNode;
        return newNode;
    }
    let curr = head;
    while (curr.next !== head) {
        // Case 1: insertVal fits between curr and curr.next
        if (curr.val <= insertVal && insertVal <= curr.next.val) break;
        // Case 2: curr is the max node and curr.next is the min node
        if (curr.val > curr.next.val) {
            if (insertVal >= curr.val || insertVal <= curr.next.val) break;
        }
        curr = curr.next;
    }
    // Insert new node
    const newNode = new _Node(insertVal, curr.next);
    curr.next = newNode;
    return head;
}