from typing import List


class Solution:
    def combine(self, n: int, k: int):
        res = []
        for s in range(1 << n):
            tmp = []
            for i in range(n):
                if str(bin(s)).count("1") == k and s & 1 << i > 0:
                    tmp.append(i + 1)
            if len(tmp) > 0:
                res.append(tmp)
        return res


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first=1, curr=[]):
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n + 1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()
        output = []
        backtrack()
        return output



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(idx, path):
            nonlocal res
            if len(path) == k:
                res.append(path)
            for i in range(idx, n + 1):
                dfs(i + 1, path + [i])
            return

        dfs(1, [])
        return res


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(startIndex, path):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(startIndex, n - (k - len(path)) + 2):  # 优化的地方
                path.append(i)  # 处理节点
                self.backtracking(i + 1, path)
                path.pop()  # 回溯，撤销处理的节点

        result = []  # 存放结果集
        self.backtracking(1, [])
        return result


if __name__ == "__main__":
    n = 5
    k = 3
    result = Solution().combine(n, k)
    print(result)
