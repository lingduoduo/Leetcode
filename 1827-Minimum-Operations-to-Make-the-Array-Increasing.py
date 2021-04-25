from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = prev = 0
        for curr in nums:
            if prev < curr:
                prev = curr
                continue
            prev += 1
            result += prev-curr                
        return result



if __name__ == '__main__':
    # nums = [1,1,1]
    # res = Solution().minOperations(nums)
    # print(res)

    # nums = [1,5,2,4,1]
    # res = Solution().minOperations(nums)
    # print(res)

    nums = [4881,2593,6819,9256,4135]
    res = Solution().minOperations(nums)
    print(res)