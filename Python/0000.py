from collections import defaultdict, deque
from typing import List
import math
import heapq
import bisect 


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        res = 0
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] < nums[j] + nums[k]:
                    res += k - j
                    j += 1
                else:
                    k -= 1

        return res

        
if __name__ == "__main__":
    print(Solution().isPalindrome(s = "A man, a plan, a canal: Panama"))
