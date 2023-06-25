from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for before, after in prerequisites:
            graph[before].append(after)

        ###0 = unknow, 1 = visiting, 2 = visited
        visited = [0] * numCourses

        for i in range(numCourses):
            if not self.dfs(graph, i, visited):
                return False
        return True

    ###can node be visited successfully?
    def dfs(self, graph, node, visit):
        if visit[node] == 1:
            return False
        if visit[node] == 2:
            return True

        visit[node] = 1
        for j in graph[node]:
            if not self.dfs(graph, j, visit):
                return False
        visit[node] = 2
        return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inbound = [0] * numCourses
        d = defaultdict(list)

        for t, f in prerequisites:
            d[f].append(t)
            inbound[t] += 1

        stack = [i for i in range(numCourses) if inbound[i] == 0]
        visited = 0
        if len(stack) == 0: return False

        while stack:
            f = stack.pop(0)
            visited += 1
            for t in d[f]:
                inbound[t] -= 1
                if inbound[t] == 0:
                    stack.append(t)
        return visited == numCourses


if __name__ == "__main__":
    res = Solution().canFinish(numCourses=2, prerequisites=[[1, 0]])
    print(res)
