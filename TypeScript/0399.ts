function calcEquation(
  equations: string[][],
  values: number[],
  queries: string[][]
): number[] {
  // Build graph
  const edge: Record<string, Array<[string, number]>> = {};
  for (let i = 0; i < equations.length; i++) {
    const [x, y] = equations[i];
    const v = values[i];
    if (!edge[x]) edge[x] = [];
    if (!edge[y]) edge[y] = [];
    edge[x].push([y, v]);
    edge[y].push([x, 1.0 / v]);
  }

  // Build connected components: each component map holds value of each node
  // relative to an arbitrary start node (value=1)
  const clusters: Array<Record<string, number>> = [];
  const visit = new Set<string>();

  for (const start of Object.keys(edge)) {
    if (visit.has(start)) continue;
    const dic: Record<string, number> = {};
    dic[start] = 1.0;
    visit.add(start);

    const q: string[] = [start];
    while (q.length > 0) {
      const cur = q.pop()!;
      for (const [n, v] of edge[cur]) {
        if (!visit.has(n)) {
          visit.add(n);
          dic[n] = dic[cur] * v; // relative value
          q.push(n);
        }
      }
    }
    clusters.push(dic);
  }

  // Answer queries
  const res: number[] = [];
  for (const [x, y] of queries) {
    // If either variable never appeared in equations, answer is -1
    if (!(x in edge) || !(y in edge)) {
      res.push(-1);
      continue;
    }

    let found = false;
    for (const cluster of clusters) {
      if (x in cluster && y in cluster) {
        res.push(cluster[y] / cluster[x]);
        found = true;
        break;
      }
    }
    if (!found) res.push(-1);
  }

  return res;
}
