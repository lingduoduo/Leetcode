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

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            alive = True

            # Only possible collision: right-moving on stack, left-moving incoming
            while alive and stack and stack[-1] > 0 and num < 0:
                if stack[-1] < -num:          # top explodes
                    stack.pop()
                    continue
                elif stack[-1] == -num:       # both explode
                    stack.pop()
                alive = False               # incoming explodes (or tied case handled)
            
            if alive:
                stack.append(num)

        return stack