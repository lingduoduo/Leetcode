
function averageOfSubtree(root: TreeNode | null): number {
    let res = 0;
    const traverse = (root: TreeNode | null): [number, number] => {
        if (!root) {
            return [0, 0];
        }
        if (!root.left && !root.right) {
            res += 1;
            return [1, root.val];
        }
        const [leftCnt, leftSum] = traverse(root.left);
        const [rightCnt, rightSum] = traverse(root.right);
        const cnt = leftCnt + rightCnt;
        const tot = leftSum + rightSum;
        if (Math.floor((tot + root.val) / (cnt + 1)) === root.val) {
            res += 1;
        }
        return [cnt + 1, tot + root.val];
    }
    
    traverse(root);
    return res;  
};