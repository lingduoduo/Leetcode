from typing import List


class Solution:
    def __init__(self) -> None:
        self.res = []
        self.path = [0]

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []

        self.dfs(graph, 0)
        return self.res

    def dfs(self, graph, root):
        if root == len(graph) - 1:
            self.res.append(self.path[:])
            return

        for node in graph[root]:
            self.path.append(node)
            self.dfs(graph, node)
            self.path.pop()


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []

        def dfs(graph, root, path):
            nonlocal res
            if root == len(graph) - 1:
                res.append(path[:])
                return

            for node in graph[root]:
                dfs(graph, node, path + [node])

        res = []
        dfs(graph, 0, [0])
        return res


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(graph, 0, [0])
        return self.res

    def dfs(self, graph, curr, path):
        if graph[curr] == []:
            self.res.append(path)
            return
        for node in graph[curr]:
            self.dfs(graph, node, path + [node])


class Solution(object):
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        res = []
        stack = [[0]]

        while stack:
            m = len(stack)
            for i in range(m):
                path = stack.pop(0)
                if path[-1] == n - 1:
                    res.append(path)
                    continue

                for node in graph[path[-1]]:
                    print(node)
                    stack.append(path + [node])
        return res


if __name__ == "__main__":
    graph = [[1, 2], [3], [3], []]
    res = Solution().allPathsSourceTarget(graph)
    print(res)
