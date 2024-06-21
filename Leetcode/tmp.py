import collections
from typing import List


class Solution:

    def rankTeams(self, votes: List[str]) -> str:
        d = collections.defaultdict(int)
        for vote in votes:
            for i, c in enumerate(vote):
                d[c] += i
        voted_names = sorted(d.keys())
        return "".join(sorted(voted_names, key=lambda x: d[x], reverse=True))


if __name__ == "__main__":
    res = Solution().rankTeams(votes = ["BCA","CAB","CBA","ABC","ACB","BAC"])
    print(res)

