# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         ####First Try
#         ###if not strs: return false
#         ###pre = min(strs, key=len)
#
#         ###for i in range(len(pre)):
#         ###	for s in strs:
#         ###		if s[i] != pre[i]:
#         ###			return pre[:i]
#         ###return pre
#
#         ####Second Try
#         ###if not strs: return ""
#         ###d = []
#         ###for s in strs:
#         ###    d.append(len(s))
#         ###d=sorted(d)
#         ###base=strs[0][:d[0]]
#         #
#         ###for i in range(len(base)):
#         ###    for j in range(len(strs)):
#         ###        if base[i]!=strs[j][i]:
#         ###            return base[:i]
#         ###return base
#
#         ###third try
#         if not strs:
#             return ""
#
#         for i in range(len(strs[0])):
#             for string in strs:
#                 if i >= len(string) or string[i] != strs[0][i]:
#                     return strs[0][:i]
#
#         return strs[0]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # this will be an answer
        pref = ''
        # find min and max words among strs
        minWord = min(strs)
        maxWord = max(strs)

        # for iteration
        i = 0
        n = min(len(minWord), len(maxWord))

        while i < n:
            # if chars are equal
            if minWord[i] == maxWord[i]:
                # add this char to the answer
                pref += minWord[i]
            else:
                # if not, break
                break
            i += 1

        return pref

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for a in zip(*strs):
            if len(set(a)) == 1:
                res += a[0]
            else:
                return res
        return res

if __name__=="__main__":
    strs=["flower","flow","flight"]
    ###strs = ["aa","a"]
    ###strs = ["dog","racecar","car"]
    results = Solution().longestCommonPrefix(strs)
    print(results)