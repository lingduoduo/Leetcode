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

function buildTree(inorder: number[], postorder: number[]): TreeNode | null {
  if (inorder.length === 0 || postorder.length === 0) return null;
  if (inorder.length === 1) return new TreeNode(inorder[0], null, null);

  const val = postorder.pop()!;                    // root value
  const idx = inorder.indexOf(val);                // split point in inorder

  const inorder_left = inorder.slice(0, idx);
  const inorder_right = inorder.slice(idx + 1);

  const size = inorder_left.length;
  const postorder_left = postorder.slice(0, size);
  const postorder_right = postorder.slice(size);

  const left = buildTree(inorder_left, postorder_left);
  const right = buildTree(inorder_right, postorder_right);

  return new TreeNode(val, left, right);
}
