class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ## First Try
        # if not strs: return false
        # pre = min(strs, key=len)

        # for i in range(len(pre)):
        # 	for s in strs:
        # 		if s[i] != pre[i]:
        # 			return pre[:i]
        # return pre

        ## Second Try
        if not strs: return ""
        d = []
        for s in strs:
            d.append(len(s))
        d=sorted(d)
        base=strs[0][:d[0]]

        for i in range(len(base)):
            for j in range(len(strs)):
                if base[i]!=strs[j][i]:
                    return base[:i]
        return base

if __name__=="__main__":
    strs=["flower","flow","flight"]
    strs = ["aa","a"]
    strs = ["dog","racecar","car"]
    results = Solution().longestCommonPrefix(strs)
    print(results)