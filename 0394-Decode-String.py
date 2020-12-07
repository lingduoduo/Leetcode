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
            print([s[i], res])
            if s[i] == '[':
                rep.append(num)
                cur.append(res)
                num = 0
                res = ''
            elif s[i] == ']':
                res = cur.pop() + res * rep.pop()
            elif s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            else:
                res += s[i]
        return res

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = cur_str = ''
        
        for cha in s:
            if cha.isdigit():
                cur_num += cha
            elif cha.isalpha():
                cur_str += cha
            elif cha == "[":
                stack.append((cur_num, cur_str))
                cur_num = cur_str = ''
            elif cha == "]":
                pre_num, pre_str = stack.pop()
                cur_str = pre_str + cur_str * int(pre_num)
        return cur_str


if __name__ == "__main__":
    ###s='3[a]2[bc]'
    ###s = "3[a2[c]]" #"accaccacc"
    s = "2[abc]3[cd]ef"  ###"abcabccdcdcdef"
    s = "100[leetcode]"
    result = Solution().decodeString(s)
    print(result)
