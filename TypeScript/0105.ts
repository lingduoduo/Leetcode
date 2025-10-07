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


function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
  if (inorder.length === 0 || preorder.length === 0) return null;
  if (inorder.length === 1) return new TreeNode(inorder[0], null, null);

  const val = preorder.shift()!;                   // root value
  const idx = inorder.indexOf(val);                // split point in inorder

  const inorder_left = inorder.slice(0, idx);
  const inorder_right = inorder.slice(idx + 1);

  const size = inorder_left.length;
  const preorder_left = preorder.slice(0, size);
  const preorder_right = preorder.slice(size);

  const left = buildTree(preorder_left, inorder_left);
  const right = buildTree(preorder_right, inorder_right);

  return new TreeNode(val, left, right);
}
