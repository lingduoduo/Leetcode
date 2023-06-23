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
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        backtrack()
        return output


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(idx, path):
            if len(path) == k:
                res.append(path)
            for i in range(idx, n):
                dfs(i + 1, path + [1 + i])

        dfs(0, [])
        return res


if __name__ == "__main__":
    n = 5
    k = 3
    result = Solution().combine(n, k)
    print(result)
