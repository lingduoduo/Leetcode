from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        l = SortedList()
        res = 0
        for a,b in zip(nums1, nums2):
            res += l.bisect_right(a - b + diff)
            l.add(a - b)
        return res