class Solution:

    def __init__(self, w: List[int]):
        self.preSum = [0] * len(w)
        self.preSum[0] = w[0]
        for i in range(1, len(w)):
            self.preSum[i] = self.preSum[i - 1] + w[i]

    def pickIndex(self) -> int:
        return bisect.bisect(self.preSum, self.preSum[-1] * random.random())
        # total = self.preSum[-1]
        # rand = random.randint(0, total - 1)
        # left, right = 0, len(self.preSum) - 1
        # while left + 1 < right:
        #     mid = (left + right) // 2
        #     if rand >= self.preSum[mid]:
        #         left = mid
        #     else:
        #         right = mid
        # if rand < self.preSum[left]:
        #     return left
        # return right