import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        regex = re.compile("[^a-z0-9]")
        sub = regex.sub("", s)
        r = list(sub)
        if r == r[::-1]:
            return True
        else:
            return False
        return sub

        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for cha in s:
            if cha.isdigit():
                strs.append(cha)
            elif cha.isalpha():
                strs.append(cha.lower())
        return strs == strs[::-1]


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    results = Solution().isPalindrome(s)
    print(results)
