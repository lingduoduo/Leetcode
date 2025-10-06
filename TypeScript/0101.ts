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

class Solution {
    isMirror(a: TreeNode | null, b: TreeNode | null): boolean {
    if (a === null && b === null) return true;
    if (a === null || b === null) return false;
    if (a.val !== b.val) return false;
    // mirror compare: left ↔ right
    return this.isMirror(a.left, b.right) && this.isMirror(a.right, b.left);
  }

    isSymmetric(root: TreeNode | null): boolean {
    if (root === null) return true;
    return this.isMirror(root.left, root.right);
    }
}