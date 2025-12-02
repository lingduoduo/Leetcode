from typing import List
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = 1
        right = max(position) - min(position) + 1
        while left < right:
            mid = left + (right - left)//2 
            cnt = 1
            start = position[0]
            for p in position:
                if p - start >= mid:
                    cnt += 1
                    start = p
                    if cnt >= m:
                        break

            if cnt < m:
                right = mid
            else:
                left = mid + 1
                
        return left - 1

if __name__ == "__main__":
    res = Solution().maxDistance(position = [1,2,3,4,7], m = 3)
    print(res)