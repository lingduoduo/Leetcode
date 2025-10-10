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

function verticalOrder(root: TreeNode | null): number[][] {
    if (!root) return [];

    const d: Map<number, number[]> = new Map();
    let stack: [TreeNode, number][] = [[root, 0]];

    while(stack.length){
        const [node, col] = stack.shift()!;
        if(!d.has(col)) d.set(col, []);
        d.get(col)!.push(node.val);
        if(node.left) stack.push([node.left, col - 1]);
        if(node.right) stack.push([node.right, col + 1]);
    }
    const keys = Array.from(d.keys()).sort((a, b) => a - b);
    const res: number[][] = [];
    for(const key of keys){
        res.push(d.get(key)!);
    }
    return res;

};