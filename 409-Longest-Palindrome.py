class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # freqs = dict()
        # for i in s:
        #     try:
        #         freqs[i] += 1
        #     except BaseException:
        #         freqs[i] = 1
        #
        # result = 0
        # odd = 0
        # for v in freqs.values():
        #     result += v // 2 * 2
        #     if v % 2 == 1:
        #         odd = 1
        # result = result + odd
        # return result

        d = {}
        for cha in s:
            if cha in d:
                d[cha] += 1
            else:
                d[cha] = 1

        even = odd = 0
        for v in d.values():
            if v % 2 == 0:
                even += v
            else:
                odd = max(odd, v)
                even += v - 1
        if odd > 0:
            return even + 1
        else:
            return even
        
if __name__ == "__main__":
    # numbers = "abccccdd"
    # numbers = "ccc"
    numbers = "bananas"
    result = Solution().longestPalindrome(numbers)
    print(result)
    print('Done')
