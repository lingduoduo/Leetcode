class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict
        # Build graph
        G = [[] for _ in range(c + 1)]
        for u, v in connections:
            G[u].append(v)
            G[v].append(u)

        # Step 1: DFS to label components
        seen = [0] * (c + 1)
        comp_id = 0

        def dfs(u, cid):
            stack = [u]
            while stack:
                x = stack.pop()
                if seen[x]: 
                    continue
                seen[x] = cid
                for nxt in G[x]:
                    if not seen[nxt]:
                        stack.append(nxt)

        for i in range(1, c + 1):
            if seen[i] == 0:
                comp_id += 1
                dfs(i, comp_id)

        # Step 2: Build todo lists, reversed for pop()
        todo = defaultdict(list)
        for i in range(c, 0, -1):
            todo[seen[i]].append(i)

        # Step 3: Process queries
        res = []
        online = [1] * (c + 1)

        for typ, x in queries:
            if typ == 1:
                if online[x]:
                    res.append(x)
                else:
                    cid = seen[x]
                    while todo[cid] and online[todo[cid][-1]] == 0:
                        todo[cid].pop()
                    res.append(todo[cid][-1] if todo[cid] else -1)
            else:  # typ == 2
                online[x] = 0

        return res
