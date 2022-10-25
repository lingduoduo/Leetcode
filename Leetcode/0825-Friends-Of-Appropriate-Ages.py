class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = collections.Counter(ages)
        ages = sorted(count.keys())
        res = 0
        for x in ages:
            for y in range(int(0.5 * x) + 7 + 1, x + 1):
                if x == y:
                    res += count[x] * (count[x] - 1)
                else:
                    res += count[x] * count[y]
        return res
