from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        for num in nums:
            diff ^= num 
        diff &= -diff

        res1 = 0 
        res2 = 0
        for num in nums:
            if num & diff == 0:
                res1 ^= num 
            else:
                res2 ^= num
        return sorted([res1, res2])

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        for num in nums:
            diff ^= num

        diff = diff & (-diff)
        group1 = [num for num in nums if num & diff]
        group2 = [num for num in nums if not num & diff]
        res = [0, 0]
        print(group1, group2)
        for num in group1:
            res[0] ^= num
        for num in group2:
            res[1] ^= num
        return res

if __name__ == "__main__":
    # res = Solution().singleNumber(nums = [1,2,1,3,2,5])
    # print(res)

    res = Solution().singleNumber(nums = [2,1,2,3,4,1])
    print(res)