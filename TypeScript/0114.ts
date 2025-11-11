function flatten(root: TreeNode | null): void {
    if (root === null) return;

    let stack = [root];
    let prev = null;
    while (stack.length){
        let node = stack.pop();
        if (prev !== null){
            prev.left = null
            prev.right = node
        }
        if (node.right) stack.push(node.right);
        if (node.left)  stack.push(node.left);
        prev = node;
    }
};



