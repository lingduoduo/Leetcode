class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]

        Input: k = 3, n = 7
                Output: [[1,2,4]]
        """
        self.res = []

        for i in range(1, 10):
            self.dfs(k - 1, n - i, i + 1, [i])

        return self.res

    def dfs(self, k, n, idx, path):
        if k == 0 and n == 0:
            self.res.append(path)

        for i in range(idx, 10):
            self.dfs(k - 1, n - i, i + 1, path + [i])
        return


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtracking(idx, cnt, tot, path):
            nonlocal res
            if cnt == k and tot == n:
                res.append(path)
                return

            for i in range(idx, 10):
                backtracking(i + 1, cnt + 1, tot + i, path + [i])

        res = []
        backtracking(1, 0, 0, [])
        return res


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []  # 存放结果集
        self.backtracking(n, k, 0, 1, [], result)
        return result

    def backtracking(self, targetSum, k, currentSum, startIndex, path, result):
        if currentSum > targetSum:  # 剪枝操作
            return  # 如果path的长度等于k但currentSum不等于targetSum，则直接返回
        if len(path) == k:
            if currentSum == targetSum:
                result.append(path[:])
            return
        for i in range(startIndex, 9 - (k - len(path)) + 2):  # 剪枝
            currentSum += i  # 处理
            path.append(i)  # 处理
            self.backtracking(
                targetSum, k, currentSum, i + 1, path, result
            )  # 注意i+1调整startIndex
            currentSum -= i  # 回溯
            path.pop()  # 回溯


if __name__ == "__main__":
    k = 3
    n = 7
    result = Solution().combinationSum3(k, n)
    print(result)

    k = 3
    n = 9
    result = Solution().combinationSum3(k, n)
    print(result)

    k = 3
    n = 15
    result = Solution().combinationSum3(k, n)
    print(result)
