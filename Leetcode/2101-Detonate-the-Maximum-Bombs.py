class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        N = len(bombs)

        # construct directed graph
        G = defaultdict(list)
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                bi = bombs[i]
                bj = bombs[j]
                if (bi[0] - bj[0]) ** 2 + (bi[1] - bj[1]) ** 2 <= bi[2] ** 2:
                    G[i].append(j)

        # apply DFS with every bomb as start point
        max_ans = 1
        for start in range(N):
            queue = [start]
            visited = set([start])
            this_ans = 0
            while queue:
                pos = queue.pop()
                this_ans += 1
                for neib in G[pos]:
                    if neib not in visited:
                        queue.append(neib)
                        visited.add(neib)
            max_ans = max(this_ans, max_ans)
            if max_ans == N:
                return N
        return max_ans
