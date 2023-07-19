from typing import List


class Solution:
    def wiggleMaxLength(self, nums) -> int:
        n = len(nums)
        if n <= 1:
            return n

        inc, dec = 1, 1
        for x in range(1, n):
            print([inc, dec])
            if nums[x] > nums[x - 1]:
                inc = dec + 1
            elif nums[x] < nums[x - 1]:
                dec = inc + 1
        return max(inc, dec)


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        res = 1
        last_wiggle = None

        for i in range(1, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and last_wiggle != 1) or (diff < 0 and last_wiggle != -1):
                res += 1
                last_wiggle = 1 if diff > 0 else -1

        return res


class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) <= 1:
            return len(nums)  # 如果数组长度为0或1，则返回数组长度
        curDiff = 0  # 当前一对元素的差值
        preDiff = 0  # 前一对元素的差值
        result = 1  # 记录峰值的个数，初始为1（默认最右边的元素被视为峰值）
        for i in range(len(nums) - 1):
            curDiff = nums[i + 1] - nums[i]  # 计算下一个元素与当前元素的差值
            # 如果遇到一个峰值
            if (preDiff <= 0 and curDiff > 0) or (preDiff >= 0 and curDiff < 0):
                result += 1  # 峰值个数加1
                preDiff = curDiff  # 注意这里，只在摆动变化的时候更新preDiff
        return result  # 返回最长摆动子序列的长度


if __name__ == "__main__":
    nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    res = Solution().wiggleMaxLength(nums)
    print(res)
