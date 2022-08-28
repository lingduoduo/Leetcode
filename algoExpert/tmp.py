from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1[:m]
        nums2 = nums2[:n]
        nums1 = nums1 + nums2
        p1 = m - 1
        p2 = n - 1
        for i in reversed(range(m + n)):
            if p1 >= 0 and p2 >= 0:
                if nums1[p1] < nums2[p2]:
                    nums1[i] = nums2[p2]
                    p2 -= 1
                else:
                    nums1[i] = nums1[p1]
                    p1 -= 1
            if p2 >= 0:
                nums1[i] = nums2[p2]
                p2 -= 1
        return nums1


if __name__ == "__main__":
    res = Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
    print(res)

    res = Solution().merge(nums1 = [1], m = 1, nums2 = [], n = 0)
    print(res)

    res = Solution().merge(nums1 = [0], m = 0, nums2 = [1], n = 1)
    print(res)