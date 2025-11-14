function distanceK(root: TreeNode | null, target: TreeNode | null, k: number): number[] {
    // adjacency list: node value -> neighbors
    const d = new Map<number, number[]>();

    const network = (parent: TreeNode | null, child: TreeNode | null) => {
        if (!child) return;

        if (parent) {
            if (!d.has(parent.val)) d.set(parent.val, []);
            if (!d.has(child.val)) d.set(child.val, []);
            d.get(parent.val)!.push(child.val);
            d.get(child.val)!.push(parent.val);
        }

        network(child, child.left);
        network(child, child.right);
    };

    if (!root || !target) return [];

    // build undirected graph
    network(null, root);

    const visited = new Set<number>();
    const q: Array<[number, number]> = [];
    const res: number[] = [];

    // BFS from target
    q.push([target.val, 0]);
    visited.add(target.val);

    while (q.length) {
        const [node, depth] = q.shift()!;

        if (depth === k) {
            res.push(node);
            // don't expand neighbors further from depth k
            continue;
        }
        if (depth > k) break; // optional small optimization

        for (const neighbor of d.get(node) || []) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                q.push([neighbor, depth + 1]);
            }
        }
    }

    return res;
}
