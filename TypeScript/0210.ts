function findOrder(numCourses: number, prerequisites: number[][]): number[] {
    const indegree = Array(numCourses).fill(0);
    const d: Map<number, number[]> = new Map(); // adjacency: y -> [x...]
    const res: number[] = [];

    // build graph
    for (const [x, y] of prerequisites) {
        indegree[x] += 1;
        if (!d.has(y)) d.set(y, []);
        d.get(y)!.push(x);
    }

    // init queue with zero-indegree nodes
    const q: number[] = [];
    for (let i = 0; i < numCourses; i++) {
        if (indegree[i] === 0) q.push(i);
    }

    // Kahn's algorithm
    while (q.length) {
        const cur = q.pop()!;              // stack/queue both fine for topo order
        res.push(cur);
        const nexts = d.get(cur) ?? [];
        for (const nxt of nexts) {
            indegree[nxt]--;
            if (indegree[nxt] === 0) q.push(nxt);
        }
    }

    return res.length === numCourses ? res : [];
}
