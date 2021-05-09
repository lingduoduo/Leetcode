class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        d = {}
        d[0] = -1
        res = 0
        cumsum = 0
        for i, num in enumerate(nums):
            if num == 0:
                cumsum -= 1
            else:
                cumsum += 1

            if cumsum in d:
                res = max(res, i-d[cumsum])
            else:
                d[cumsum]=i

        return res


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = cnt = 0
        d = {0: 0}
        
        for i, num in enumerate(nums, 1):
            cnt += 1 if num == 0 else -1
                
            if cnt in d:
                res = max(res, i-d[cnt])
            else:
                d[cnt]=i
                
        return res
        
