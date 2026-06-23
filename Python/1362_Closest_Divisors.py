class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        res = []
        min_diff = float("inf")

        for x in [num + 1, num + 2]:
            for a in range(int(x ** 0.5), 0, -1):
                if x % a == 0:
                    b = x // a
                    if b - a < min_diff:
                        min_diff = b - a
                        res = [a, b]
                    break

        return res