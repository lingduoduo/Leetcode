class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n-1
        while left <= right:
            mid = left + (right-left)//2
            h = max(h, min(citations[mid], n-mid))
            if citations[mid] < n-mid:
                left = mid + 1
            else:
                right = mid + 1
        return h