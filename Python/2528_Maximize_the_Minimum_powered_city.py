from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        diff_base = [0] * (n + 1)
        for i, power in enumerate(stations):
            left = max(0, i - r)
            right = min(n, i + r + 1)   
            diff_base[left] += power
            diff_base[right] -= power

        def can_achieve(target: int) -> bool:
            diff = diff_base.copy()  
            total = 0                
            remaining = k            

            for i in range(n):
                total += diff[i]     
                if total < target:
                    need = target - total
                    if remaining < need:
                        return False
                    remaining -= need
                    end = min(n, i + 2 * r + 1)
                    diff[end] -= need
                    total += need   

            return True

        lo, hi = 0, sum(stations) + k 
        ans = 0

        while lo <= hi:
            mid = (lo + hi) // 2
            if can_achieve(mid):
                ans = mid     
                lo = mid + 1
            else:
                hi = mid - 1  

        return ans
