class Solution:
   def racecar(self, target: int) -> int:
       #1. Initialize double ended queue as 0 moves, 0 position, +1 velocity
       queue = collections.deque([(0, 0, 1)])
       while queue:
           # (moves) moves, (pos) position, (vel) velocity)
           moves, pos, vel = queue.popleft()
           if pos == target:
               return moves
           #2. Always consider moving the car in the direction it is already going
           queue.append((moves + 1, pos + vel, 2 * vel))
           #3. Only consider changing the direction of the car if one of the following conditions is true
           #   i.  The car is driving away from the target.
           #   ii. The car will pass the target in the next move.
           if (pos + vel > target and vel > 0) or (pos + vel < target and vel < 0):
               queue.append((moves + 1, pos, -vel / abs(vel)))
