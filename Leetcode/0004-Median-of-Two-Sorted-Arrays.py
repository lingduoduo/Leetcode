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
# class Solution(object):
# def findMedianSortedArrays(self, nums1, nums2):
#     lst = nums1 + nums2
#     lst.sort()
#     median = 0
#     if len(lst) % 2 == 1:
#         median = lst[(len(lst) // 2)]
#     else:
#         median = (float(lst[len(lst) // 2] + lst[(len(lst) // 2) - 1]) / 2)
#     return median

#         int M = nums1.size();
#         int N = nums2.size();
#         if (M > N) return findMedianSortedArrays(nums2, nums1);
#         int L = M + N;

#         int k = (L + 1) / 2; //总共左边需要多少个元素
#         int l = 0, r = M; // 对于nums1而言
#         int m1 = 0, m2 = 0;
#         while (l < r) {
#             m1 = l + (r - l) / 2; // nums1的分割位置，左边的元素个数
#             m2 = k - m1; // nums2的分割位置，左边的元素个数
#             if (nums1[m1] < nums2[m2 - 1]) {
#                 l = m1 + 1;
#             } else {
#                 r = m1;
#             }
#         }
#         m1 = l;
#         m2 = k - l;
#         double c1 = max(m1 <= 0 ? INT_MIN : nums1[m1 - 1],
#                         m2 <= 0 ? INT_MIN : nums2[m2 - 1]);
#         if (L & 1)
#             return c1;
#         double c2 = min(m1 >= M ? INT_MAX : nums1[m1],
#                         m2 >= N ? INT_MAX : nums2[m2]);
#         return (c1 + c2 ) / 2;
#     }
# };    

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        n1 = len(nums1)
        n2 = len(nums2)
        k = (n1+n2+1)//2
        
        left = 0
        right = n1
        while (left<right):
            m1 = left + (right-left)//2
            m2 = k - m1
            if (nums1[m1]<nums2[m2-1]):
                left = m1+1
            else:
                right = m1
        m1 = left
        m2 = k-left
        c1 = max(float("-inf") if m1<=0 else nums1[m1-1], float("-inf") if m2<=0 else nums2[m2-1])
        if (n1+n2)%2 == 1:
            return c1
        c2 = min(float("inf") if m1>=n1 else nums1[m1], float("inf") if m2>=n2 else nums2[m2])
        return (c1+c2)/2
      

