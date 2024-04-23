import collections
from typing import List
from collections import defaultdict

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        idx = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[idx]:
                cnt += 1
                if cnt == 2:
                    idx += 1
            else:
                cnt = 1
                idx += 1
                nums[idx] = nums[i]
        return idx + 1
        
if __name__ == "__main__":
    res = Solution().removeDuplicates(nums = [1,1,1,2,2,3])
    print(res)  

