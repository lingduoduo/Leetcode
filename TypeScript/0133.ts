function cloneGraph(node: _Node | null): _Node | null {
	if (node === null) return null;
    const d = new Map<_Node, _Node>();
    const queue: _Node[] = [node];
    d.set(node, new _Node(node.val));

    while(queue.length) {
        const cur = queue.shift()!;
        for (const child of cur.neighbors) {
            if (!d.has(child)) {
                d.set(child, new _Node(child.val));
                queue.push(child);
            }
            d.get(cur)!.neighbors.push(d.get(child)!);
        }
    }
    return d.get(node)!;
};
