from typing import List


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
        if target == 0:
            self.res.append(path)
            return
        for i in range(idx, len(candidates)):
            if candidates[i] > target:
                break
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]])


class Solution(object):
    def combinationSum2(self, candidates, target):
        def dfs(cur, path):
            if cur == 0:
                res.append(path)
            for idx, num in enumerate(candidates):
                if num > cur:
                    break
                if (path and num == path[-1]) or visited[idx] == 1:
                    continue
                visited[idx] = 0
                dfs(cur - num, path + [num])
                visited[idx] = 1

        res = []
        visited = [0] * len(candidates)
        candidates.sort()
        dfs(target, [])
        return res


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target, index, path):
            if target < 0:
                return
            elif target == 0:
                res.append(path)
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                dfs(target - candidates[i], i + 1, path + [candidates[i]])

        candidates.sort()
        res = []
        dfs(target, 0, [])
        return res


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    result = Solution().combinationSum2(candidates, 8)
    print(result)

    # candidates = [1]
    # result = Solution().combinationSum2(candidates, 1)
    # print(result)
