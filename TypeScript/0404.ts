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

function sumOfLeftLeaves(root: TreeNode | null): number {
    if (root === null) return 0;
    if (root.left === null && root.right === null) return 0;
    if (root.left.left == null && root.left.left == null) return root.left.val;
    return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right);
};