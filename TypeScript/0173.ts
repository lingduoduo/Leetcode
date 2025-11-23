class BSTIterator {
    private stack: TreeNode[] = [];

    constructor(root: TreeNode | null) {
        this.pushLeft(root);
    }

    // Push all left children
    private pushLeft(node: TreeNode | null): void {
        while (node !== null) {
            this.stack.push(node);
            node = node.left;
        }
    }

    next(): number {
        // Pop the smallest element
        const node = this.stack.pop()!;
        const val = node.val;

        // If the node has a right subtree, push its left spine
        if (node.right !== null) {
            this.pushLeft(node.right);
        }

        return val;
    }

    hasNext(): boolean {
        return this.stack.length > 0;
    }
};
