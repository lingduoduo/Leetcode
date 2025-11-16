function treeToDoublyList(root: _Node | null): _Node | null {
	if (!root) return null;
    const stack: _Node[] = [];
    const dummy = new _Node(-1);
    let prev: _Node = dummy;
    let node: _Node | null = root;

    while (stack.length > 0 || node) {
        while (node) {
            stack.push(node);
            node = node.left;
        }
        node = stack.pop()!;
        node.left = prev;
        prev.right = node;
        prev = node;
        node = node.right;
    }

    dummy.right!.left = prev;
    prev.right = dummy.right;

    return dummy.right;
};


