class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] >= 0:
                pre = stack.pop()
                if asteroid == -pre:
                    asteroid = None
                    break
                elif -asteroid < pre:
                    asteroid = pre
            if asteroid != None:
                stack.append(asteroid)
        return stack
