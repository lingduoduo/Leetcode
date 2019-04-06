class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        rep = []
        cur = []
        res = ''
        num = 0

        for i in range(len(s)):
            print([s[i],res])
            if s[i] == '[':
                rep.append(num)
                cur.append(res)
                num = 0
                res = ''
            elif s[i] == ']':
                res = cur.pop() + res * rep.pop()
            elif s[i].isdigit():
                num = num*10 + ord(s[i]) - ord('0')
            else:
                res += s[i]
        return res

if __name__ == "__main__":
    # s='3[a]2[bc]'
    # s = "3[a2[c]]" #"accaccacc"
    s = "2[abc]3[cd]ef" #"abcabccdcdcdef"
    s="100[leetcode]"
    result = Solution().decodeString(s)
    print(result)
