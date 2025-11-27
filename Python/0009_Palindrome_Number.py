class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        """
        :type x: int
        :rtype: bool
        """
        input = x
        if x < 0:
            return False
        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x = x // 10
        if res == input:
            return True
        else:
            return False


if __name__ == "__main__":
    results = Solution().isPalindrome(88888)
    print(results)
    results = Solution().isPalindrome(10)
    print(results)
