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

function convertBST(root: TreeNode | null): TreeNode | null {
  if (root === null) return root;

  let pre = 0; 
  function traverse(node: TreeNode | null): void {
    if (node === null) return;
    traverse(node.right);
    pre += node.val;
    node.val = pre;
    traverse(node.left);
  }

  traverse(root);
  return root;
}
