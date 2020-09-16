class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        res = ["0"]*n
        size = k**n
        visited = set()
        visited.add("".join(res))
        if self.dfs(res, visited, size, n, k):
            return "".join(res)
        return ""

    def dfs(self, res, visited, size, n, k):
        if len(visited )==size:
            return True
        node = "".join(res[len(res)-n+1:])
        for i in range(k):
            node = node + str(i)
            if node not in visited:
                res.append(str(i))
                visited.add(node)
                if self.dfs(res, visited, size, n, k):
                    return True
                res.pop()
                visited.remove(node)
            node = node[:-1]