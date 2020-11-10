# class Solution(object):
#     def combinationSum(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         candidates = sorted(candidates)
#         self.res = []
#         self.dfs(candidates, target, 0, [])
#         return self.res
    
#     def dfs(self, candidates, target, idx, path):
#         if target == 0:
#             self.res.append(path)
#             return
        
#         for i in range(idx, len(candidates)):
#             if candidates[i] > target:
#                 break
#             self.dfs(candidates, target -
#                      candidates[i], i, path +
#                      [candidates[i]])

class Solution(object):
    def combinationSum(self, candidates, target: int):
        def dfs(cur, path):
            if cur == 0:
                res.append(path)
            for n in candidates:
                if n > cur:
                    break
                if path and n < path[-1]:
                    continue
                dfs(cur - n, path + [n])
                
        res = []
        candidates.sort()
        dfs(target, [])
        return res

if __name__ == "__main__":
    nums = [2, 3, 6, 7]
    result = Solution().combinationSum(nums, 7)
    print(result)
