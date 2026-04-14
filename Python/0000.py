from collections import defaultdict, deque
from typing import List
import math
import heapq


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        prev = []  # store last round's subsets
        
        for i, num in enumerate(nums):
            cur = []

            if i > 0 and nums[i] == nums[i - 1]:
                for pre in prev:   # ✅ use prev instead of cur
                    cur.append(pre + [num])
            else:
                for pre in res:
                    cur.append(pre + [num])
            
            prev = cur            # ✅ update prev
            res += cur
        
        return res

                    
if __name__ == "__main__":
    res = Solution().subsetsWithDup(nums = [1,2,2])
    print(res)
