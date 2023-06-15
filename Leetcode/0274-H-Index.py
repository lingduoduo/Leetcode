class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        h = 0
        for k, v in enumerate(citations):
            h = max(h, min(n - k, v))
        return h
