class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        res = 0
        scores = 0

        left = 0
        right = len(tokens) - 1

        while left <= right:
            if tokens[left] <= P:
                P -= tokens[left]
                scores += 1
                res = max(res, scores)
                left += 1
            else:
                if scores < 1:
                    break
                else:
                    scores -= 1
                    P += tokens[right]
                    right -= 1
        return res
