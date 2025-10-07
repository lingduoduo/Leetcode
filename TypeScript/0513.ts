class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

function findBottomLeftValue(root: TreeNode | null): number {
    if (root === null) return 0;

    const queue: TreeNode[] = [];
    queue.push(root);
    let res = 0;

    while (queue.length) {
        const size = queue.length;
        for (let i = 0; i < size; i++) {
            const node = queue.shift()!; // `!` ensures non-null after shift
            if (i === 0) res = node.val; // first element in this level = leftmost
            if (node.left !== null) queue.push(node.left);
            if (node.right !== null) queue.push(node.right);
        }
    }

    return res;
}
