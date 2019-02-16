class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        result = []
        for word in words:
            result.append(word[::-1])
        return " ".join(result)