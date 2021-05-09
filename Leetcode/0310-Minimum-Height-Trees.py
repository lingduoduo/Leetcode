class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n ==1:
            return [0]

        leaves = collections.defaultdict(set)
        for u, v in edges:
            leaves[u].add(v)
            leaves[v].add(u)

        que = collecitons.deque()
        for v, vs in leaves.items():
            if len(vs) == 1:
                que.append(v)
                
        while n>2:
            n = n - len(que)
            for _ in range(len(que)):
                u = que.popleft()
                for v in leaves[u]:
                    leaves[v].remove(u)
                    if len(leaves[v]) == 1:
                        que.append(v)
        return list(que)

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        edge = [set() for _ in range(n)]
        for u, v in edges:
            edge[u].add(v)
            edge[v].add(u)
        q = [x for x in range(n) if len(edge[x]) < 2]
        tmp = []
        while True:
            for node in q:
                for n in edge[node]:
                    edge[n].remove(node)
                    if len(edge[n]) == 1:
                        tmp.append(n)
            if not tmp:
                break
            tmp, q = [], tmp
        return q