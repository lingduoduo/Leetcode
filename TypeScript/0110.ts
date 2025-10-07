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
function getDepth(root: TreeNode | null): number{
    if (root === null) return 0;
    if (root.left === null && root.right === null) return 1;
    return 1 + Math.max(getDepth(root.left), getDepth((root.right)))
}

function isBalanced(root: TreeNode | null): boolean {
  if (root === null) return true;
  const left = getDepth(root.left);
  const right = getDepth(root.right);
  if (Math.abs(left - right) > 1) return false;        // allow diff 0 or 1
  return isBalanced(root.left) && isBalanced(root.right); // subtrees must be balanced too
}