import collections


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        d = collections.Counter()
        maxf = 0
        res = 0
        for i in range(len(answerKey)):
            d[answerKey[i]] += 1
            maxf = max(maxf, d[answerKey[i]])
            if res < maxf + k:
                res += 1
            else:
                d[answerKey[i - res]] -= 1
        return res


if __name__ == "__main__":
    res = Solution().maxConsecutiveAnswers(answerKey="TTFF", k=2)
    print(res)
