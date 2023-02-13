class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        @cache
        def fn(i, cost):
            """Return sum of subsequence closest to target."""
            if cost >= target or i == len(toppingCosts): return cost
            return min(fn(i + 1, cost), fn(i + 1, cost + toppingCosts[i]), key=lambda x: (abs(x - target), x))

        ans = inf
        toppingCosts *= 2
        for cost in baseCosts:
            ans = min(ans, fn(0, cost), key=lambda x: (abs(x - target), x))
        return ans 