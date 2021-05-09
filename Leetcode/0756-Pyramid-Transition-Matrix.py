from typing import List
import collections
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        d = collections.defaultdict(list)
        for idx, val in enumerate(allowed):
            d[val[:2]].append(val[2])
        return self.helper(bottom, "", d)

    def helper(self, curr, above, d):
        if len(curr) == 2 and len(above) == 1:
            return True

        if len(above) == len(curr) - 1:
            return self.helper(above, "", d)

        pos = len(above)
        base = curr[pos:pos+2]
        if base in d:
            for cha in d[base]:
                if self.helper(curr, above+cha, d):
                    return True
        return False

if __name__ == '__main__':
    # bottom = "XYZ"
    # allowed = ["XYD", "YZE", "DEA", "FFF"]
    # res = Solution().pyramidTransition(bottom, allowed)
    # print(res)

    # bottom = "AABA"
    # allowed = ["AAA","AAB","ABA","ABB","BAC"]
    # res = Solution().pyramidTransition(bottom, allowed)
    # print(res)

    bottom = "CCC"
    allowed = ["CBB","ACB","ABD","CDB","BDC","CBC","DBA","DBB","CAB","BCB","BCC","BAA","CCD","BDD","DDD","CCA","CAA","CCC","CCB"]
    res = Solution().pyramidTransition(bottom, allowed)
    print(res)

