class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        p = re.compile(r'\s{2,}')
        s = p.sub(" ", s)
        words = s.split(" ")
        return " ".join(words[::-1])
