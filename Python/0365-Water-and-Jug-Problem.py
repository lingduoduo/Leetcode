class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        return z == 0 or (x + y >= z and z % self.gcd(x, y) == 0)

    def gcd(self, x, y):
        print([x, y])
        return x if y == 0 else self.gcd(y, x % y)

from collections import deque
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        q = deque([0])
        seen = set()
        steps = [x, -y, x, -y]

        while q:
            cur = q.popleft()
            for step in steps:
                tot = cur + step 
                if tot == target:
                    return True
                if tot not in seen and 0 <= tot <= x + y:
                    seen.add(tot)
                    q.append(tot)
        return False        

if __name__ == "__main__":
    g = Solution().gcd(3, 5)
    print(g)
