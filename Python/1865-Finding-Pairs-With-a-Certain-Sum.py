from typing import List

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.d = {}
        for num in nums2:
            if num in self.d:
                self.d[num] += 1
            else:
                self.d[num] = 1

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.d[old_val] -= 1
        if self.d[old_val] == 0:
            del self.d[old_val]
        self.nums2[index] += val
        if self.nums2[index] not in self.d:
            self.d[self.nums2[index]] = 1
        else:
            self.d[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        res = 0
        for num in self.nums1:
            complement = tot - num
            if complement in self.d:
                res += self.d[complement]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)