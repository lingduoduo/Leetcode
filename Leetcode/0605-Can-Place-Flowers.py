class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if sum(flowerbed[0:2]) == 0:
            flowerbed[0] = 1
            n -= 1

        if sum(flowerbed[-2:]) == 0:
            flowerbed[-1] = 1
            n -= 1

        for i in range(1, len(flowerbed) - 1):
            print(flowerbed[i - 1: i + 2])
            if sum(flowerbed[i - 1: i + 2]) == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i, num in enumerate(flowerbed):
            if num == 1: continue
            if i > 0 and flowerbed[i - 1] == 1: continue
            if i < len(flowerbed) - 1 and flowerbed[i + 1] == 1: continue
            flowerbed[i] = 1
            n -= 1
        return n <= 0
