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


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    results = Solution().isPalindrome(s)
    print(results)
