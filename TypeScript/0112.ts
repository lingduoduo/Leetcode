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

function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
    if (root === null) return false;
    const stack: Array<[TreeNode, number]> = [];
    stack.push([root, targetSum]);

    while (stack.length){
        const [node, target] = stack.pop()!;
        if (node.left === null && node.right === null && node.val === target) return true;
        if (node.left !== null) stack.push([node.left, target - node.val]);
        if (node.right !== null) stack.push([node.right, target - node.val]);
    }
    return false
};
