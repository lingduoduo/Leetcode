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

function binaryTreePaths(root: TreeNode | null): string[] {
  function trace(node: TreeNode, path: string, res: string[]) {
    path += String(node.val);
    if (node.left === null && node.right === null) {
      res.push(path);
      return;
    }
    if (node.left !== null) trace(node.left, path + '->', res);
    if (node.right !== null) trace(node.right, path + '->', res);
  }

  const res: string[] = [];
  if (root === null) return res;
  trace(root, '', res);
  return res;
}
