from typing import List
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        i = 0
        res = []
        while i < len(s):
            if i not in indices:
                res.append(s[i])
                i += 1
            else:
                ind = indices.index(i)
                source = sources[ind]
                target = targets[ind]
                if source == s[i: i+len(source)]:
                    res.append(target)
                else:
                    res.append(s[i: i+len(source)])
                i += len(source)
        return ''.join(res)

if __name__ == '__main__':
    res = Solution().findReplaceString(s="abcd", indices=[0, 2], sources=["a", "cd"], targets=["eee", "ffff"])
    print(res)
    res = Solution().findReplaceString(s="abcd", indices=[0, 2], sources=["ab","ec"], targets=["eee","ffff"])
    print(res)
