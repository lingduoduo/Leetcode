class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = left + (right-left)//2
            count = 1
            total = 0
            for weight in weights:
                total += weight
                if total>mid:
                    count += 1
                    total = weight
                    
            if count > D:
                left = mid + 1
            else:
                right = mid
        return left 
        