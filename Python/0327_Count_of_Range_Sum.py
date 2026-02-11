from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        pre = [0]
        s = 0
        for x in nums:
            s += x
            pre.append(s)

        def sort_count(lo: int, hi: int) -> int:
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            cnt = sort_count(lo, mid) + sort_count(mid, hi)

            # count cross pairs: left in [lo, mid), right in [mid, hi)
            j = k = mid
            for i in range(lo, mid):
                while k < hi and pre[k] - pre[i] < lower:
                    k += 1
                while j < hi and pre[j] - pre[i] <= upper:
                    j += 1
                cnt += j - k

            # merge sorted halves
            res = []
            i, r = lo, mid
            while i < mid and r < hi:
                if pre[i] <= pre[r]:
                    res.append(pre[i]); i += 1
                else:
                    res.append(pre[r]); r += 1
            res.extend(pre[i:mid])
            res.extend(pre[r:hi])
            pre[lo:hi] = res
            return cnt

        return sort_count(0, len(pre))
