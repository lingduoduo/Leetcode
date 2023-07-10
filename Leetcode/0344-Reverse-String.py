class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        # 该方法已经不需要判断奇偶数，经测试后时间空间复杂度比用 for i in range(len(s)//2)更低
        # 因为while每次循环需要进行条件判断，而range函数不需要，直接生成数字，因此时间复杂度更低。推荐使用range
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)

        for i in range(n // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]
        return s


if __name__ == "__main__":
    input = ["h", "e", "l", "l", "o"]
    ###input = ["e", "l", "l", "o"]
    result = Solution().reverseString(input)
    print(result)
