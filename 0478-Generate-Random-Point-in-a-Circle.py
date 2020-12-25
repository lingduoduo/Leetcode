import random
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        newradius = math.sqrt(random.random()) * self.radius
        newthelta = random.random() * 2 * 3.1415926 
        newx = self.x_center + newradius*math.cos(newthelta)
        newy = self.y_center + newradius*math.sin(newthelta)
        return [newx, newy]



# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()