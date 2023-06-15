class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        ###minSpeed = 1
        ###maxSpeed = max(piles) + 1

        ###while minSpeed < maxSpeed:
        ###    mid = minSpeed + (maxSpeed - minSpeed) // 2
        ###    h = 0
        ###    for p in piles:
        ###        h += (p + mid - 1) // mid
        ###    if h > H:
        ###        minSpeed = mid + 1
        ###    else:
        ###        maxSpeed = mid
        ###return minSpeed

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / mid)
            if hour <= H:
                right = mid
            else:
                left = mid + 1
        return left
