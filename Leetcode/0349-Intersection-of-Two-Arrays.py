from typing import List


class Solution(object):
    def intersection(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        ref = set(nums2)
        res = set()
        for i in range(len(nums1)):
            if nums1[i] in ref:
                res.add(nums1[i])
        return res


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = [0] * 1001
        count2 = [0] * 1001
        result = []
        for i in range(len(nums1)):
            count1[nums1[i]] += 1
        for j in range(len(nums2)):
            count2[nums2[j]] += 1
        for k in range(1001):
            if count1[k] * count2[k] > 0:
                result.append(k)
        return result


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
