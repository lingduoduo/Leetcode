class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0
        while i<len(encoded1) and j<len(encoded2):
            val1, freq1 = encoded1[i]
            val2, freq2 = encoded2[j]
            freq = min(freq1, freq2)
            if res and res[-1][0] == val1 * val2:
                res[-1][1] += freq
            else:
                res.append([val1 * val2, freq])
            encoded1[i][1] -= freq
            encoded2[j][1] -= freq
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1
        return res