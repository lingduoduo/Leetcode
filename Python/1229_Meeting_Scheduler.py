class Solution:
    def minAvailableDuration(
        self, slots1: List[List[int]], slots2: List[List[int]], duration: int
    ) -> List[int]:
        slots1.sort()
        slots2.sort()
        idx1 = idx2 = 0

        while idx1 < len(slots1) and idx2 < len(slots2):
            intersect_left = max(slots1[idx1][0], slots2[idx2][0])
            intersect_right = min(slots1[idx1][1], slots2[idx2][1])
            if intersect_right - intersect_left >= duration:
                return [intersect_left, intersect_left + duration]
            if slots1[idx1][1] < slots2[idx2][1]:
                idx1 += 1
            else:
                idx2 += 1
        return []
