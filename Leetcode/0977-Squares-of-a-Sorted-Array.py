from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            res.append(num * num)
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


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, i = 0, len(nums) - 1, len(nums) - 1
        res = [float("inf")] * len(nums)  # 需要提前定义列表，存放结果
        while l <= r:
            if nums[l] ** 2 < nums[r] ** 2:  # 左右边界进行对比，找出最大值
                res[i] = nums[r] ** 2
                r -= 1  # 右指针往左移动
            else:
                res[i] = nums[l] ** 2
                l += 1  # 左指针往右移动
            i -= 1  # 存放结果的指针需要往前平移一位
        return res


if __name__ == "__main__":
    res = Solution().sortedSquares(nums=[-4, -1, 0, 3, 10])
    print(res)

    res = Solution().sortedSquares(nums=[-5, -3, -2, -1])
    print(res)

    res = Solution().sortedSquares(nums=[0, 2])
    print(res)
