class Solution:
    def maxArea(self, height) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left = 0
        right = len(height) - 1
        while left < right:
            h = min(height[left], height[right])
            res = max(res, h * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(height))
