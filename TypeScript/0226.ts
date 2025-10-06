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
    invertTree(root: TreeNode | null): TreeNode | null {
        if (root === null) return null;
        const left = root.left;                  // preserve original left
        root.left = this.invertTree(root.right); // swap subtrees
        root.right = this.invertTree(left);
        return root;
    }
}