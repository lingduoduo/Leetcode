class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = 0
        sum = 0
        while sum < target:
            k += 1
            sum += k
        d = sum - target
        if d % 2 == 0:
            return k
        return k + 1 + (k % 2)
