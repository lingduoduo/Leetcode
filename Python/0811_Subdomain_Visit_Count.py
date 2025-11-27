import collections
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = collections.Counter()
        for cp in cpdomains:
            count, domain = cp.split()
            count = int(count)
            frags = domain.split(".")
            for i in range(len(frags)):
                res[".".join(frags[i:])] += count
        return [f"{v} {k}" for k, v in res.items()]


if __name__ == "__main__":
    cpdomains = ["9001 discuss.leetcode.com"]
    res = Solution().subdomainVisits(cpdomains)
    print(res)

    cpdomains = [
        "900 google.mail.com",
        "50 yahoo.com",
        "1 intel.mail.com",
        "5 wiki.org",
    ]
    res = Solution().subdomainVisits(cpdomains)
    print(res)
