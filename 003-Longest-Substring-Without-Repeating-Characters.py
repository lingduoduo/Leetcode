if __name__ == "__main__":

    result = Solution().lengthOfLongestSubstring("abcabcbb")
    result = Solution().lengthOfLongestSubstring("au")
    result = Solution().lengthOfLongestSubstring("abba")
    print(result)




class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) <=1:
            return 1

        ## First try
        # longest = 0
        # start = -1
        # location = [-1 for i in range(256)]

        # for i,v in enumerate(s):
        #     if location[ord(v)] > start:
        #         start = location[ord(v)]
        #     longest = max(longest, i-start)
        #     location[ord(v)] = i
        # return longest

        ## Second try
        if not s:
            return 0
        if len(s) <=1:
            return 1

        result = 0
        left = -1
        n = len(s)
        d = {}

        for i in range(len(s)):
            if s[i] in d and d[s[i]]>left:
                left = d[s[i]]
            d[s[i]]=i
            result = max(result, i-left)
        return result
