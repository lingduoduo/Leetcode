function rob(root: TreeNode | null): number {
    const dfs(node : TreeNode | null): [number, number] => {
        if (!node) {
            // l1 = 0 (skip), l2 = 0 (take)
            return [0, 0];
        }

        const [left_l1, left_l2] = dfs(node.left);
        const [right_l1, right_l2] = dfs(node.right);

        // If we take this node, we cannot take children:
        const take = node.val + left_l1 + right_l1;   // l2

        // If we skip this node, children choose best:
        const skip = Math.max(left_l1, left_l2) + Math.max(right_l1, right_l2);  // l1

        // You wanted to return (l, l1) where l = max(l1, l2)
        const best = Math.max(skip, take);

        // return (l1=skip, l2=take)
        return [skip, take];
    };

    const [skip, take] = dfs(root);
    return Math.max(skip, take);
    
};
