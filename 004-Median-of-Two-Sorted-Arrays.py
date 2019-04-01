class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lenA, lenB = len(nums1), len(nums2)
        if (lenA + lenB) % 2 == 1:
            return self.getKth(nums1, nums2, (lenA + lenB) / 2 + 1)
        else:
            return (self.getKth(nums1, nums2, (lenA + lenB) / 2) +
                    self.getKth(nums1, nums2, (lenA + lenB) / 2 + 1)) * 0.5

    def getKth(self, A, B, k):
        lenA, lenB = len(A), len(B)
        if lenA > lenB:
            return self.getKth(B, A, k)

        if lenA == 0:
            return B[k - 1]

        if k == 1:
            return min(A[0], B[0])

        pa = min(k / 2, lenA)
        pb = k - pa

        if A[pa - 1] < B[pb - 1]:
            return self.getKth(A[pa:], B, k - pa)
        elif A[pa - 1] > B[pb - 1]:
            return self.getKth(A, B[pb:], k - pb)
        else:
            return A[pa - 1]
