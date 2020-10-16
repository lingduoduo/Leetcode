import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        regex = re.compile('[^a-z0-9]')
        sub = regex.sub('', s)
        r = list(sub)
        if r == r[::-1]:
           return True
        else:
           return False
        return sub
        
        left = 0
        right = len(s)-1
        while left < right:
            while left<right and not s[left].isalnum():
                left += 1
            while left<right and not s[right].isalnum():
                right -=1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    results = Solution().isPalindrome(s)
    print(results)
