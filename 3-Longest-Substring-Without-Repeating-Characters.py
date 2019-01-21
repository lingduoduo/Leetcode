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

        longest = 0
        start = -1
        location = [-1 for i in range(256)]
        
        for i,v in enumerate(s):
            if location[ord(v)] > start:
                start = location[ord(v)]
            longest = max(longest, i-start)
            location[ord(v)] = i
        return longest

if __name__ == "__main__":    

    result = Solution().lengthOfLongestSubstring("abcabcbb")
    result = Solution().lengthOfLongestSubstring("au")
    result = Solution().lengthOfLongestSubstring("abba")
    print(result)
