from typing import List
import collections
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res = []
        dmap = collections.defaultdict(list)
        for w in d:
            dmap[w[0]].append((0, w))

        for c in s:
            wlist = dmap[c]
            del dmap[c]

            for i, w in wlist:
                if i + 1 == len(w):
                    res.append(w)
                else:
                    dmap[w[i + 1]].append((i + 1, w))
        
        if not res: return ''
        maxl = len(max(res, key = len))
        return min(w for w in res if len(w) == maxl)

if __name__ == '__main__':
	s = "abpcplea"
	d = ["ale","apple","monkey","plea"]
	res = Solution().findLongestWord(s, d)
	print(res)