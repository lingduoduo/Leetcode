
// Definition for a binary tree node.
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


function minCameraCover(root: TreeNode | null): number {
    let res = 0;
    function rec(node: TreeNode | null): number{
        if (node === null) return 2;

        const left = rec(node.left);
        const right = rec(node.right);

        if (left === 0 || right === 0){
            res += 1;
            return 1;
        } else if (left === 1 || right === 1){
            return 2;
        } else return  0;
    }

    if (rec(root) === 0) res++;
    return res;
};
