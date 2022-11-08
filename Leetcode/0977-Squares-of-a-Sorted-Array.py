from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            res.append(num*num)
        res.sort()
        return res

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = map(lambda x: x**2, nums)
        return sorted(res)


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result

if __name__ == "__main__":
    res = Solution().sortedSquares(nums = [-4,-1,0,3,10])
    print(res)

    res = Solution().sortedSquares(nums=[-5,-3,-2,-1])
    print(res)

    res = Solution().sortedSquares(nums=[0,2])
    print(res)
