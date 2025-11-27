from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        que = collections.deque()
        step = 0
        goal = (1 << n) - 1
        visited = [[0 for j in range(1 << n)] for i in range(n)]
        for i in range(n):
            que.append((i, 1 << i))
        while que:
            s = len(que)
            for i in range(s):
                node, state = que.popleft()
                if state == goal:
                    return step
                if visited[node][state]:
                    continue
                visited[node][state] = 1
                for nextnode in graph[node]:
                    que.append((nextnode, state | (1 << nextnode)))
            step += 1
        return step
