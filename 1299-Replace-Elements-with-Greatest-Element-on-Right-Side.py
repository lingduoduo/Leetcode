class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        tmp = arr[::-1]
        m = tmp[0]
        res = [-1]
        for i in range(len(tmp)-1):
            m = max(m, tmp[i])
            res.append(m)
        return res[::-1]
            