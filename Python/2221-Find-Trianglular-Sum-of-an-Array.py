from typing import List
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        q = deque(nums)
        while q:
            first = q.popleft()                 # O(1)
            for _ in range(len(q)):             # fixed length per level
                second = q.popleft()            # O(1)
                q.append((first + second) % 10)
                first = second
        return first
                
if __name__ == "__main__":
    s = Solution()
    print(s.triangularSum([5])) 