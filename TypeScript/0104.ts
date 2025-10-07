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

class Solution{
    maxDepth(root: TreeNode | null): number {
        if (root === null) return 0;
        if (root.left === null && root.right === null) return 1;
        return Math.max(this.maxDepth(root.left), this.maxDepth(root.right)) + 1
    }
}