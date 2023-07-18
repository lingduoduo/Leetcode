from typing import List


class Solution(object):
    def combinationSum(self, candidates, target):
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
            self.dfs(candidates, target - candidates[i], i, path + [candidates[i]])


class Solution:
    def combinationSum(self, candidates, target: int):
        def dfs(cur, path):
            if cur == 0:
                res.append(path)

            for candidate in candidates:
                if candidate > cur:
                    break
                if path and candidate < path[-1]:
                    continue
                dfs(cur - candidate, path + [candidate])

        res = []
        candidates.sort()
        dfs(target, [])
        return res


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(total, startIndex, path):
            if total > target:
                return
            if total == target:
                result.append(path[:])
                return

            for i in range(startIndex, len(candidates)):
                backtracking(total + candidates[i], i, path + [candidates[i]])

        result = []
        backtracking(0, 0, [])
        return result


if __name__ == "__main__":
    nums = [2, 3, 6, 7]
    result = Solution().combinationSum(nums, 7)
    print(result)
