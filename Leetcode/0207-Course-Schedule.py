class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:

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
        edge = defaultdict(list)
        for x, y in prerequisites:
            inbound[x] += 1
            edge[y].append(x)
        stack = [i for i in range(numCourses) if inbound[i] == 0]
        visited = 0
        while stack:
            cur = stack.pop()
            visited += 1
            for node in edge[cur]:
                inbound[node] -= 1
                if inbound[node] == 0:
                    stack.append(node)
        return visited == numCourses
