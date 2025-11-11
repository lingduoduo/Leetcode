function findRedundantConnection(edges: number[][]): number[] {
    const graph = new Map<number, Set<number>>();

    function dfs(source: number, target: number, seen: Set<number>): boolean {
        if (source === target) return true;
        seen.add(source);

        const neighbors = graph.get(source);
        if (!neighbors) return false;

        for (const neighbour of neighbors) {
            if (!seen.has(neighbour)) {
                if (dfs(neighbour, target, seen)) return true;
            }
        }
        return false;
    }

    for (const [u, v] of edges) {
        // if both nodes already exist and there's already a path between them,
        // then [u, v] is the redundant edge.
        if (graph.has(u) && graph.has(v) && dfs(u, v, new Set<number>())) {
            return [u, v];
        }

        if (!graph.has(u)) graph.set(u, new Set<number>());
        if (!graph.has(v)) graph.set(v, new Set<number>());

        graph.get(u)!.add(v);
        graph.get(v)!.add(u);
    }

    return [];
}
