function allPathsSourceTarget(graph: number[][]): number[][] {
      if (graph.length === 0) return [];

      const n = graph.length;
      const res: number[][] = [];

      function dfs(start: number, path: number[]): void {
        if (start === n - 1) {
          res.push([...path]);       // push a copy
          return;
        }
        const end = graph[start];     // neighbors
        for (let i = 0; i < end.length; i++) {
          const next = end[i];
          path.push(next);            // go to neighbor
          dfs(next, path);            // recurse on neighbor
          path.pop();                 // backtrack
        }
      }

      dfs(0, [0]); // start path with source node 0
      return res;
}