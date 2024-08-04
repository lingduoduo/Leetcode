class Solution:
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        return self.dfs(price, special, needs, {})

    def dfs(self, price, special, needs, d):
        val = sum(price[i] * needs[i] for i in range(len(needs)))
        for spec in special:
            remains = [needs[j] - spec[j] for j in range(len(needs))]
            if min(remains) >= 0:
                val = min(
                    val,
                    d.get(
                        tuple(needs), spec[-1] + self.dfs(price, special, remains, d)
                    ),
                )
        d[tuple(needs)] = val
        return val
