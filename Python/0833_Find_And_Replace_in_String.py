from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        toReplace = {}
        for i in range(len(sources)):
            s_idx = indices[i]
            if s[s_idx:s_idx+len(sources[i])] == sources[i]:
                toReplace[s_idx] = i

        res = []
        i = 0
        while i < len(s):
            if i in toReplace:
                res.append(targets[toReplace[i]])
                i += len(sources[toReplace[i]])
            else:
                res.append(s[i])
                i += 1
        return ''.join(res)



if __name__ == "__main__":
    res = Solution().findReplaceString(
        s="abcd", indices=[0, 2], sources=["a", "cd"], targets=["eee", "ffff"]
    )
    print(res)
    res = Solution().findReplaceString(
        s="abcd", indices=[0, 2], sources=["ab", "ec"], targets=["eee", "ffff"]
    )
    print(res)
