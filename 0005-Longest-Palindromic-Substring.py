class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ###print(s)
        ###if len(s) <= 1:
        ###    return s
        #
        ###result = ""
        ###size = 0
        #
        ###for i in range(len(s)):
        ###    indices = [k for k, x in enumerate(s) if x == s[i] and k > i]
        #
        ###    for j in indices:
        ###        if s[i:(j + 1)] == s[i:(j + 1)][::-1] and (j - i + 1) > size:
        ###            size = j - i + 1
        ###            result = s[i:(j + 1)]
        #
        ###if size < 2:
        ###    return s[1]
        ###else:
        ###    return result
        
        n = len(s)
        
        def getlen(l, r):
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            return r-l-1
        
        start = 0
        length = 0
        for i in range(n):
            cur = max(getlen(i,i), getlen(i, i+1))
            if cur <= length:
                continue
            length = cur
            start = i - (cur -1)//2
        return s[start: start+length]


class Solution(object):

    def longestPalindrome(self, s):       
      # 1.先判斷該字串是否為一個字母，或是本身是迴文
      if (len(s) <= 1) or s == s[::-1]:
          return s
      else:
          # 紀錄開始的位置
          startIndex = 1
          # 紀錄目前最大迴文的長度
          maxLen = 1
          # 開始跑迴圈
          for i in range(1 ,len(s)):
              # 跑第一圈時，odd要找 s[-1:2]，event要找 s[0:2]
              # 跑第二圈時，odd要找 s[0:3]，event要找 s[1:3]
              # 跑第三圈時，odd要找 s[1:4]，event要找 s[2:4]
              odd = s[i - maxLen - 1 : i + 1]
              even = s[i - maxLen : i + 1]
              # 判斷odd是否為迴文
              if i - maxLen - 1 >= 0 and odd == odd[::-1]:
                  startIndex = i - maxLen - 1
                  maxLen += 2
              elif i - maxLen >= 0 and even == even[::-1]:
                  startIndex = i - maxLen
                  maxLen += 1
      return s[startIndex : startIndex + maxLen]
        
if __name__ == "__main__":
    print(Solution().longestPalindrome("abbae"))
    # print(Solution().longestPalindrome("bb"))
    # print(Solution().longestPalindrome("cbbd"))
    # print('Done')

