class Solution:
    def customSortString(self, S: str, T: str) -> str:
        pos = collections.defaultdict(int)
        for i in range(len(S)):
            pos[S[i]] = i
        res = sorted(T, key = lambda x: pos[x])
        return "".join(res)
        