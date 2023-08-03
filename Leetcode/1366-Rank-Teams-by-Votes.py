from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        d = {}

        for vote in votes:
            for i, char in enumerate(vote):
                if char not in d:
                    d[char] = [0] * len(vote)
                d[char][i] += 1

        voted_names = sorted(d.keys())
        return "".join(sorted(voted_names, key=lambda x: d[x], reverse=True))


if __name__ == "__main__":
    res = Solution().rankTeams(votes=["ABC", "ACB", "ABC", "ACB", "ACB"])
    print(res)
