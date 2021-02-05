class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = 5.5 * (hour * 60 + minutes) % 360
        return angle if angle <= 180 else 360 - angle