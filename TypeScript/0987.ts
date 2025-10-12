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

function verticalTraversal(root: TreeNode | null): number[][] {
  if (root === null) return [];

  const map = new Map<number, Array<{ row: number; val: number }>>();
  const stack: Array<{ node: TreeNode | null; col: number; row: number }> = [
    { node: root, col: 0, row: 0 },
  ];

  while (stack.length) {
    const { node, col, row } = stack.pop()!;
    if (node) {
      const arr = map.get(col) ?? [];
      arr.push({ row, val: node.val });
      map.set(col, arr);

      stack.push({ node: node.left, col: col - 1, row: row + 1 });
      stack.push({ node: node.right, col: col + 1, row: row + 1 });
    }
  }

  const res: number[][] = [];
  const keys = Array.from(map.keys()).sort((a, b) => a - b);

  for (const key of keys) {
    const sorted = map.get(key)!.sort(
      (a, b) => a.row - b.row || a.val - b.val
    );
    res.push(sorted.map((x) => x.val));
  }

  return res;
}
