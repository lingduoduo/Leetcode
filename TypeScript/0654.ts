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

function constructMaximumBinaryTree(nums: number[]): TreeNode | null {
  if (nums.length === 0) return null;

  const max_val = Math.max(...nums);        // <-- spread, not Math.max(nums)
  const max_idx = nums.indexOf(max_val);

  const left = constructMaximumBinaryTree(nums.slice(0, max_idx));
  const right = constructMaximumBinaryTree(nums.slice(max_idx + 1));

  return new TreeNode(max_val, left, right);
}