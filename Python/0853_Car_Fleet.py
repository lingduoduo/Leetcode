class Solution:
   def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
       pairs = []
       for x in range(len(speed)):
           pairs.append([position[x], speed[x]])
       pairs = sorted(pairs)[::-1]
      
       stack = []
       for p, s in pairs:
           time = (target - p) / s
           stack.append(time)
           if len(stack) >= 2 and stack[-1] <= stack[-2]:
               stack.pop()
      
       return len(stack)
