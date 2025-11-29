class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val === undefined ? 0 : val;
        this.left = left === undefined ? null : left;
        this.right = right === undefined ? null : right;
    }
}

class Codec {
    // Encodes a tree to a single string.
    serialize(root: TreeNode | null): string {
        const res: string[] = [];

        const preorder = (node: TreeNode | null) => {
            if (!node) {
                res.push("#");
                return;
            }
            res.push(String(node.val));
            preorder(node.left);
            preorder(node.right);
        };

        preorder(root);
        return res.join(",");
    }

    // Decodes your encoded data to tree.
    deserialize(data: string): TreeNode | null {
        if (!data) return null;

        const vals = data.split(",");
        let index = 0;

        const build = (): TreeNode | null => {
            if (index === vals.length) return null;
            const val = vals[index++];
            if (val === "#") return null;

            const node = new TreeNode(Number(val));
            node.left = build();
            node.right = build();
            return node;
        };

        return build();
    }
}
