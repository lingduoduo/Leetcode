class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        self.res = []
        self.dfs(candidates, target, 0, [])
        return self.res

    def dfs(self, candidates, target, idx, path):
        # print([candidates, target, idx, path])
        if target == 0:
            self.res.append(path)
            return
        for i in range(idx, len(candidates)):
            if candidates[i] > target:
                break
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates,
                     target - candidates[i],
                     i + 1,
                     path + [candidates[i]])


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    result = Solution().combinationSum2(candidates, 8)
    print(result)
