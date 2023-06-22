from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n1 = len(nums1)
        n2 = len(nums2)
        k = (n1 + n2 + 1) // 2

        left = 0
        right = n1
        while left < right:
            m1 = left + (right - left) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2 - 1]:
                left = m1 + 1
            else:
                right = m1
        m1 = left
        m2 = k - left
        c1 = max(
            float("-inf") if m1 <= 0 else nums1[m1 - 1],
            float("-inf") if m2 <= 0 else nums2[m2 - 1],
        )
        if (n1 + n2) % 2 == 1:
            return c1
        c2 = min(
            float("inf") if m1 >= n1 else nums1[m1],
            float("inf") if m2 >= n2 else nums2[m2],
        )
        return (c1 + c2) / 2


import heapq


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final = heapq.merge(nums1, nums2)
        final = list(final)
        if len(final) % 2 != 0:
            return final[len(final) // 2]
        else:
            left = int(len(final) / 2) - 1
            right = int(len(final) / 2)
            return (final[left] + final[right]) / 2


def findMedianSortedArrays(self, nums1, nums2):
    a, b = sorted((nums1, nums2), key=len)
    m, n = len(a), len(b)
    mid = (m + n - 1) / 2
    # Determine i, j that a[0:i] + b[0:j] (exclusive) is the most small "after" numbers.
    # There could multiple pairs of such (i, j) if there are some duplicated numbers.
    # Each each such pair satisfies the following criteria at the same time:
    # 1) i + j == mid
    # 2) (j>=1 and a[i] >= b[j-1]) or j==0
    # 3) (i>=1 and b[j] >= a[i-1]) or i==0
    lo, hi = 0, m
    while lo < hi:
        i = (lo + hi) // 2
        j = mid - i
        cond1 = (j >= 1 and a[i] >= b[j - 1]) or j == 0
        cond2 = (i >= 1 and b[j] >= a[i - 1]) or i == 0
        if cond1 and cond2:
            lo = i
            break
        elif not cond1:
            assert cond2
            lo = i + 1
        else:
            assert cond1
            hi = i
    i = lo
    j = mid - i
    nextfew = sorted(a[i : i + 2] + b[j : j + 2])
    return (nextfew[0] + nextfew[1 - (m + n) % 2]) // 2.0


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partitionA = (left + right) // 2
            partitionB = (m + n + 1) // 2 - partitionA

            maxLeftA = float("-inf") if partitionA == 0 else nums1[partitionA - 1]
            minRightA = float("inf") if partitionA == m else nums1[partitionA]
            maxLeftB = float("-inf") if partitionB == 0 else nums2[partitionB - 1]
            minRightB = float("inf") if partitionB == n else nums2[partitionB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                else:
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                right = partitionA - 1
            else:
                left = partitionA + 1
