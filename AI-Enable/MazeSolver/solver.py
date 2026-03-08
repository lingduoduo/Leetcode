"""You'll implement this."""

from typing import List, Optional

from maze import Maze, Position
from collections import deque

class Solver:
    def __init__(self, maze: Maze) -> None:
        self.maze = maze

    def solve(self) -> Optional[List[Position]]:
        from collections import deque
        
        start = self.maze.start
        end = self.maze.end
        
        # BFS queue: each element is (position, path_to_position)
        queue = deque([(start, [start])])
        visited = {start}
        
        while queue:
            current_pos, path = queue.popleft()
            
            # Check if we reached the end
            if current_pos == end:
                return path
            
            # Check all four directions manually using is_valid_move
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
            
            for dr, dc in directions:
                neighbor = Position(current_pos.row + dr, current_pos.col + dc)
                
                # Use is_valid_move to check if this move is allowed
                if self.maze.is_valid_move(current_pos, neighbor) and neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))
        
        # No path to end found - return list with just start position
        return [start]
