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

function rightSideView(root: TreeNode | null): number[] {
    const res: number[] = [];
    const q: TreeNode[] = [];
    if (root) q.push(root);

    while (q.length) {
        const curr: number[] = [];
        const n = q.length;

        for (let i = 0; i < n; i++) {
            const node = q.shift()!;
            curr.push(node.val);
            if (node.left !== null) q.push(node.left);
            if (node.right !== null) q.push(node.right);
        }
        res.push(curr.pop()!);
    }
    return res;
}