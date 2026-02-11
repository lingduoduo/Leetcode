import collections
from typing import List

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


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        MAX = 120
        d = [0] * (MAX + 1)
        for a in ages:
            d[a] += 1

        # prefix[i] = number of people with age <= i
        prefix = [0] * (MAX + 1)
        for a in range(1, MAX + 1):
            prefix[a] = prefix[a - 1] + d[a]

        res = 0
        for a in range(15, MAX + 1):  # ages < 15 can never send valid requests
            if d[a] == 0:
                continue

            # valid b must satisfy: b > 0.5*a + 7 and b <= a
            low = math.floor(0.5 * a + 7)
            valid_b = prefix[a] - prefix[low]  # count of ages in (low, a]
            # each of the cnt[a] people can send to (valid_b - 1) people (exclude self when b == a)
            res += d[a] * (valid_b - 1)

        return res