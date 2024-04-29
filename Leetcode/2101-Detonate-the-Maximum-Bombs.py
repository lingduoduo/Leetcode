from collections import defaultdict

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        # construct directed graph
        d = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                bi = bombs[i]
                bj = bombs[j]
                if (bi[0] - bj[0]) ** 2 + (bi[1] - bj[1]) ** 2 <= bi[2] ** 2:
                    d[i].append(j)

        # apply DFS with every bomb as start point
        res = 1
        for start in range(N):
            queue = [start]
            visited = set([start])
            curr = 0
            while queue:
                pos = queue.pop()
                curr += 1
                for neighbor in d[pos]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            res = max(curr, res)
            if res == n:
                return n
        return res
