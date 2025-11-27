class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        strs = [cha for cha in s]
        ref = ["i", "e", "a", "o", "u", "A", "E", "I", "O", "U"]
        left = 0
        right = len(s) - 1
        while left < right:
            while strs[left] not in ref and left < right:
                left += 1
            while strs[right] not in ref and left < right:
                right -= 1
            strs[left], strs[right] = strs[right], strs[left]
            left += 1
            right -= 1
        return "".join(strs)


if __name__ == "__main__":
    ###s="hello"
    ###result = Solution().reverseVowels(s)
    ###print(result)
    s = "aA"
    result = Solution().reverseVowels(s)
    print(result)
