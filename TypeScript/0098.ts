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

function isValidBST(root: TreeNode | null): boolean {
  let maxVal: number = -Infinity; // or use `let prev: number | null = null;`

  function inorderTraverse(node: TreeNode | null): boolean {
    if (node === null) return true;
    if (!inorderTraverse(node.left)) return false;
    if (node.val <= maxVal) return false; // BST must be strictly increasing
    maxVal = node.val;
    return inorderTraverse(node.right);
  }
  return inorderTraverse(root);
}