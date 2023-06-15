class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        nums = list(num)
        for i in range(len(num)):
            d = nums[-1]
            if int(d) % 2 == 1:
                return "".join(nums)
            else:
                nums.pop()
        return ""


if __name__ == "__main__":
    res = Solution().largestOddNumber(num="4206")
    print(res)
