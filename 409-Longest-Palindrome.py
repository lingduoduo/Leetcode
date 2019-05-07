class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freqs = dict()
        for i in s:
            try:
                freqs[i] += 1
            except BaseException:
                freqs[i] = 1
        
        result = 0
        odd = 0
        for v in freqs.values():
            result += v // 2 * 2
            if v % 2 == 1:
                odd = 1
        result = result + odd
        return result


if __name__ == "__main__":
    numbers = "abccccdd"
    result = Solution().longestPalindrome(numbers)
    print(result)
    print('Done')
