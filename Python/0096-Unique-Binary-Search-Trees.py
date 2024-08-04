class Solution:
    def numTrees(self, n: int) -> int:
        self.d = {}
        return self.dfs(n)

    def dfs(self, n):
        if n in self.d:
            return self.d[n]
        if n == 0 or n == 1:
            return 1

        res = 0
        for i in range(1, n + 1):
            res += self.dfs(i - 1) * self.dfs(n - i)
        self.d[n] = res
        return res


class Solution:
    def numTrees(self, n: int) -> int:
        res = [0] * (n + 1)
        res[0] = res[1] = 1

        for i in range(2, n + 1):
            for j in range(0, i):
                res[i] += res[j] * res[i - j - 1]

        return res[n]


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)  # 创建一个长度为n+1的数组，初始化为0
        dp[0] = 1  # 当n为0时，只有一种情况，即空树，所以dp[0] = 1
        for i in range(1, n + 1):  # 遍历从1到n的每个数字
            for j in range(1, i + 1):  # 对于每个数字i，计算以i为根节点的二叉搜索树的数量
                dp[i] += dp[j - 1] * dp[i - j]  # 利用动态规划的思想，累加左子树和右子树的组合数量
        return dp[n]  # 返回以1到n为节点的二叉搜索树的总数量
