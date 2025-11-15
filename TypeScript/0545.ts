function boundaryOfBinaryTree(root: TreeNode | null): number[] {
    if (!root) return [];

    function leftBoundary(node: TreeNode | null): number[] {
        if (!node) return [];
        if (!node.left && !node.right) return [];

        if (node.left) {
            return [node.val, ...leftBoundary(node.left)];
        } else {
            return [node.val, ...leftBoundary(node.right)];
        }
    }

    function leaves(node: TreeNode | null): number[] {
        if (!node) return [];
        if (!node.left && !node.right) return [node.val];
        return [...leaves(node.left), ...leaves(node.right)];
    }

    function rightBoundary(node: TreeNode | null): number[] {
        if (!node) return [];
        if (!node.left && !node.right) return [];

        if (node.right) {
            return [...rightBoundary(node.right), node.val];
        } else {
            return [...rightBoundary(node.left), node.val];
        }
    }

    return [
        root.val,
        ...leftBoundary(root.left),
        ...leaves(root.left),
        ...leaves(root.right),
        ...rightBoundary(root.right)
    ];
}
