from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k == n: return sum(cardPoints)
        
        steps = n - k
        total = sum(cardPoints)
        cur = sum(cardPoints[:steps])
        res = cur
        for i in range(steps, n):
            cur += cardPoints[i] - cardPoints[i - steps]
            res = min(res, cur)
        
        return total - res

if __name__ == "__main__":
    res = Solution().maxScore(cardPoints = [1,79,80,1,1,1,200,1], k = 3)
    print(res)

