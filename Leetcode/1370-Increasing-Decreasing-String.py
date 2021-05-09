import collections
class Solution:
    def sortString(self, s: str) -> str:
        d = collections.defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        s_cha = sorted(d.keys())

        res = ''
        while len(res) < len(s):
            for i in range(len(s_cha)):
                if len(d[s_cha[i]]) > 0:
                    res += s[d[s_cha[i]].pop(0)]
            for i in reversed(range(len(s_cha))):
                if len(d[s_cha[i]]) > 0:
                    res += s[d[s_cha[i]].pop(0)]
        return res  
        
if __name__ == '__main__':
    s = "aaaabbbbcccc"
    res = Solution().sortString(s)
    print(res)

    s = "rat"
    res = Solution().sortString(s)
    print(res)

    s = "leetcode"
    res = Solution().sortString(s)
    print(res)

    s = "spo"
    res = Solution().sortString(s)
    print(res)