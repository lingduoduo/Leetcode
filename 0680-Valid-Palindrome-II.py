# class Solution(object):
#     def validPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         start = 0
#         end = len(s) - 1
        
#         isPalindrome = lambda input: input == input[::-1]
#         while start < end:
#             if s[start] != s[end]:
#                 case1 = s[:start] + s[start + 1:]
#                 case2 = s[:end] + s[end + 1:]
#                 return isPalindrome(case1) or isPalindrome(case2)
#             start += 1
#             end -= 1
#         return True

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
