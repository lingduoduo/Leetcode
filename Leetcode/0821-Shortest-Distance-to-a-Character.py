class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        idx = []
        for i in range(len(S)):
            if S[i] == C:
                idx.append(i)
                
        res = []
        for i in range(len(S)):
            tmp = float("inf")
            for j in idx:
                tmp = min(tmp, abs(i-j))
            res.append(tmp)
        return res
                
            