class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val === undefined ? 0 : val);
        this.left = (left === undefined ? null : left);
        this.right = (right === undefined ? null : right);
    }
}

function lowestCommonAncestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null {
	if (root === null || root === p || root === q) return root;
    if (root.val > Math.max(p!.val, q!.val)) {
        return lowestCommonAncestor(root.left, p, q);
    } else if (root.val < Math.min(p!.val, q!.val)) {
        return lowestCommonAncestor(root.right, p, q);
    } else {
        return root;
    }
};
