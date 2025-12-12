from collections import defaultdict, deque
from typing import List

class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        
        edge = defaultdict(list)
        for i in range(len(equations)):
            x, y = equations[i]
            v = values[i]
            edge[x].append((y, v))
            edge[y].append((x, 1.0 / v))
        clusters = []
        visit = set()
        for x, y in equations:
            dic = {}
            if x not in visit:
                start = x
                visit.add(start)
                dic[start] = 1
                q = [start]
                while q:
                    cur = q.pop()
                    for n, v in edge[cur]:
                        if n not in visit:
                            visit.add(n)
                            q.append(n)
                            dic[n] = dic[cur] * v
            clusters.append(dic)

        res = []
        for x, y in queries:
            for cluster in clusters:
                if x in cluster and y in cluster:
                    res.append(cluster[y] / cluster[x])
                    break
            else:
                res.append(-1)
        return res


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1.0 / v))

        def bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0

            q = deque([(src, 1.0)])
            seen = {src}

            while q:
                cur, val = q.popleft()
                if cur == dst:
                    return val
                for nxt, w in graph[cur]:
                    if nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, val * w))
            return -1.0

        return [bfs(a, b) for a, b in queries]
    

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 1) Build mapping: variable -> index
        idx_set = set()
        for a, b in equations:
            idx_set.add(a)
            idx_set.add(b)

        d = {v: i for i, v in enumerate(idx_set)}
        n = len(d)

        # 2) Build directed edges (u, v, w) meaning u / v = w
        edges = []
        for (a, b), val in zip(equations, values):
            u, v = d[a], d[b]
            edges.append((u, v, val))
            edges.append((v, u, 1.0 / val))

        # 3) Bellman-Ford per query
        def bellman(src: str, dst: str) -> float:
            if src not in d or dst not in d:
                return -1.0
            if src == dst:
                return 1.0

            dist = [None] * n
            dist[d[src]] = 1.0

            for _ in range(n - 1):
                changed = False
                for u, v, w in edges:
                    if dist[u] is None:
                        continue
                    new_val = dist[u] * w
                    if dist[v] is None:
                        dist[v] = new_val
                        changed = True
                if not changed:
                    break

            ans = dist[d[dst]]
            return ans if ans is not None else -1.0

        return [bellman(a, b) for a, b in queries]
