class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = dict()
        
        for i in range(len(s) - 9):
            if s[i: (i + 10)] in d:
                d[s[i: (i + 10)]] += 1
            else:
                d[s[i: (i + 10)]] = 1
        
        return [key for key, val in d.items() if val > 1]


if __name__ == "__main__":
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    s = "AAAAAAAAAAA"
    result = Solution().findRepeatedDnaSequences(s)
    print(result)
