class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0

        words = s.split(" ")

        for i in range(len(words)):
            if words[len(words) - i - 1] != '':
                return len(words[len(words) - i - 1])
        return 0
