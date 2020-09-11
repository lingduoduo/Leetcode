###class Solution(object):
###first try
###    def findMedianSortedArrays(self, nums1, nums2):
    ###    """
    ###    :type nums1: List[int]
    ###    :type nums2: List[int]
    ###    :rtype: float
    ###    """
    ###    lenA, lenB = len(nums1), len(nums2)
    ###    if (lenA + lenB) % 2 == 1:
    ###        return self.getKth(nums1, nums2, (lenA + lenB) / 2 + 1)
    ###    else:
    ###        return (self.getKth(nums1, nums2, (lenA + lenB) / 2) +
    ###                self.getKth(nums1, nums2, (lenA + lenB) / 2 + 1)) * 0.5
    #
    ###def getKth(self, A, B, k):
    ###    lenA, lenB = len(A), len(B)
    ###    if lenA > lenB:
    ###        return self.getKth(B, A, k)
    #
    ###    if lenA == 0:
    ###        return B[k - 1]
    #
    ###    if k == 1:
    ###        return min(A[0], B[0])
    #
    ###    pa = min(k / 2, lenA)
    ###    pb = k - pa
    #
    ###    if A[pa - 1] < B[pb - 1]:
    ###        return self.getKth(A[pa:], B, k - pa)
    ###    elif A[pa - 1] > B[pb - 1]:
    ###        return self.getKth(A, B[pb:], k - pb)
    ###    else:
    ###        return A[pa - 1]

###second try
class Solution(object):
def findMedianSortedArrays(self, nums1, nums2):
    lst = nums1 + nums2
    lst.sort()
    median = 0
    if len(lst) % 2 == 1:
        median = lst[(len(lst) // 2)]
    else:
        median = (float(lst[len(lst) // 2] + lst[(len(lst) // 2) - 1]) / 2)
    return median

###class Solution:
###    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
###        if len(nums1)>len(nums2):
###            nums1, nums2 = nums2, nums1
###        n1 = len(nums1)
###        n2 = len(nums2)
#
###        k = (n1+n2+1)//2
#
###        left = 0
###        right = n1
#
###        while (left<right):
###            m1 = left + (right-left)//2
###            m2 = k - m1
###            if (nums1[m1]<nums2[m2-1]):
###                left = m1+1
###            else:
###                right = m1
#
###        m1 = left
###        m2 = k-m1
#
###        c1 = max(if m1<0)
###...

