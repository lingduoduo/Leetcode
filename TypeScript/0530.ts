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

function getMinimumDifference(root: TreeNode | null): number {
  const stack: TreeNode[] = [];
  let cur: TreeNode | null = root;
  let pre: TreeNode | null = null;
  let res = Infinity;

  while (stack.length || cur !== null) {
    if (cur !== null) {
      stack.push(cur);
      cur = cur.left;
    } else {
      cur = stack.pop()!;                 // visit node
      if (pre !== null) {
        res = Math.min(res, cur.val - pre.val);
      }
      pre = cur;                          // update previous regardless
      cur = cur.right;                    // move to right subtree
    }
  }

  return res === Infinity ? 0 : res;      // in case tree has <2 nodes
}
