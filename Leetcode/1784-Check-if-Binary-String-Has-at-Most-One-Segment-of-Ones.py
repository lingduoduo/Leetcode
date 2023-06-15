class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return False if "10" in s and "01" in s else True
