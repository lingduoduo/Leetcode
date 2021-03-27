from typing import List
import collections
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        target = collections.defaultdict(int)

        for word in B:
            for k, v in collections.Counter(word).items():
                target[k] = max(target[k], v)

        res = []
        for word in A:
            ct = collections.Counter(word)
            for k, v in target.items():
                if k not in ct or ct[k] < v:
                    break
            else:
                res.append(word)
        return res

if __name__ == '__main__':
     A = ["amazon","apple","facebook","google","leetcode"]
     B = ["ec","oc","ceo"]
     res = Solution().wordSubsets(A, B)
     print(res)