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

function findMode(root: TreeNode | null): number[] {
    let res: number[] = [];
    let pre: TreeNode | null = null;
    let count = 0;
    let mode = 0;

    function searchBST(node: TreeNode | null): void {
        if (node === null) return;

        searchBST(node.left);

        if (pre && pre.val === node.val) count++;
        else count = 1;

        if (count > mode) {
            mode = count;
            res = [node.val];
        } else if (count === mode) {
            res.push(node.val);
        }

        pre = node;
        searchBST(node.right);
    }

    searchBST(root);
    return res;
}
