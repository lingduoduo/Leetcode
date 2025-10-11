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

function deleteNode(root: TreeNode | null, key: number): TreeNode | null {
  if (root === null) return null;

  if (root.val === key) {
    // 0 or 1 child cases
    if (root.left === null && root.right === null) return null;
    if (root.left === null) return root.right;
    if (root.right === null) return root.left;

    // 2 children: find inorder successor (min in right subtree)
    let node = root.right;
    while (node.left !== null) {
      node = node.left;
    }
    node.left = root.left
    return root.right;
  } else if (root.val > key) {
    root.left = deleteNode(root.left, key);
  } else {
    root.right = deleteNode(root.right, key);
  }
  return root;
}
