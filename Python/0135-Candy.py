from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1 for i in range(len(ratings))]

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i + 1] < ratings[i] and candies[i + 1] >= candies[i]:
                candies[i] = candies[i + 1] + 1

        return sum(candies)


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candyVec = [1] * len(ratings)

        # 从前向后遍历，处理右侧比左侧评分高的情况
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candyVec[i] = candyVec[i - 1] + 1

        # 从后向前遍历，处理左侧比右侧评分高的情况
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candyVec[i] = max(candyVec[i], candyVec[i + 1] + 1)

        # 统计结果
        result = sum(candyVec)
        return result
