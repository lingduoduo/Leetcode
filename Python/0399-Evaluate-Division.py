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
