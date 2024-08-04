from typing import List


class Solution:
    def jump(self, nums) -> int:
        if not nums or len(nums) < 2:
            return 0

        res = 0
        steps = 0
        reach = 0
        for i in range(len(nums) - 1):
            reach = max(reach, i + nums[i])
            if i == steps:
                res += 1
                steps = reach
        return res


class Solution:
    def jump(self, nums: List[int]) -> int:
        result = [float("inf")] * len(nums)  # 初始化结果数组，初始值为一个较大的数
        result[0] = 0  # 起始位置的步数为0

        for i in range(len(nums)):  # 遍历数组
            for j in range(nums[i] + 1):  # 在当前位置能够跳跃的范围内遍历
                if i + j < len(nums):  # 确保下一跳的位置不超过数组范围
                    result[i + j] = min(result[i + j], result[i] + 1)  # 更新到达下一跳位置的最小步数

        return result[-1]  # 返回到达最后一个位置的最小步数


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    results = Solution().jump(nums)
    print(results)
