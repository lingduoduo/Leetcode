function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    const inbound: number[] = new Array(numCourses).fill(0);        // in-degrees
    const adj: number[][] = Array.from({ length: numCourses }, () => []); // adjacency list
    const stack: number[] = [];

    for (let [t, f] of prerequisites){
        adj[f].push(t);
        inbound[t] += 1;
    }

    for (let i = 0; i < numCourses; i ++){
        if (inbound[i] === 0) stack.push(i);
    }
    let visited = 0;
    if (stack.length === 0) return false;
    while (stack.length){
        let node = stack.pop();
        visited += 1;
        for (let neighbour of adj[node]){
            inbound[neighbour] -= 1;
            if (inbound[neighbour] === 0){
                stack.push(neighbour)
            }
        }
    }
    return visited == numCourses;
};