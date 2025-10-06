// Definition for a binary tree node.
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

function postorderTraversal(root: TreeNode | null): number[] {
    const res: number[] = [];

    const inorder = (node: TreeNode | null): void => {
        if (node === null) return;
        if (node.left != null) inorder(node.left);
        res.push(node.val);
        if (node.right != null) inorder(node.right);

    }

    inorder(root);
    return res;
};
