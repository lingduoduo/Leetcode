import collections


class Solution:
    def subdomainVisits(self, cpdomains):
        d = collections.Counter()
        for domains in cpdomains:
            num, domain = domains.split(" ")
            dstr = domain.split(".")[::-1]

            while len(dstr) > 0:
                s = ".".join(dstr[::-1])
                d[s] += int(num)
                dstr.pop()
        return [str(v) + " " + k for k, v in d.items()]


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
