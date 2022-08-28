class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                news = list(s)
                news.pop(left)
                if news == news[::-1]:
                    return True

                news = list(s)
                news.pop(right)
                if news == news[::-1]:
                    return True
                return False
        return True

if __name__ == '__main__':
    s = "abc"
    results = Solution().validPalindrome(s)
    print(results)
