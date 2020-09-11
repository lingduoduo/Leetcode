class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ###if s == '':
        ###    return 0
        #
        ###words = s.split(" ")
        #
        ###for i in range(len(words)):
        ###    if words[len(words) - i - 1] != '':
        ###        return len(words[len(words) - i - 1])
        ###return 0
        
        count = 0
        local_count = 0
        
        for i in range(len(s)):
            if s[i] == " ":
                local_count=0
            else:
                local_count += 1
                count = local_count
        return count
