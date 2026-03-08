"""
Provides sample mazes for testing and benchmarking.
get_simple_maze() is useful for basic path rendering tests.
get_small_maze() is useful when developing your Solver.
get_medium_maze() tests BFS efficiency.
get_directional_maze() tests one-way passage handling.
get_huge_maze() tests optimization (bidirectional BFS).
"""

from typing import List

from maze import Maze


def get_simple_maze() -> Maze:
    grid = [
        "#####",
        "#S..#",
        "#.#.#",
        "#..E#",
        "#####",
    ]
    return Maze(grid)


def get_small_maze() -> Maze:
    grid = [
        "#######",
        "#S....#",
        "#.###.#",
        "#.#...#",
        "#.#.#.#",
        "#...#E#",
        "#######",
    ]
    return Maze(grid)


def get_medium_maze() -> Maze:
    grid = [
        "###############",
        "#S............#",
        "#.###########.#",
        "#.#.........#.#",
        "#.#.#######.#.#",
        "#.#.#.....#.#.#",
        "#.#.#.###.#.#.#",
        "#.#.#.#...#.#.#",
        "#.#.#.#.###.#.#",
        "#.#.#.#.....#.#",
        "#.#.#.#######.#",
        "#.#.#.........#",
        "#.#.###########",
        "#.............E",
        "###############",
    ]
    return Maze(grid)


def get_directional_maze() -> Maze:
    grid = [
        "#######",
        "#S.>..#",
        "#.###.#",
        "#.<...#",
        "#.###.#",
        "#....E#",
        "#######",
    ]
    return Maze(grid)


def get_directional_maze_blocked() -> Maze:
    grid = [
        "#######",
        "#S.<..#",
        "###.###",
        "#E....#",
        "#######",
    ]
    return Maze(grid)


def get_anywhere_start_end_maze() -> Maze:
    grid = [
        "#######",
        "#..E..#",
        "#.###.#",
        "#S....#",
        "#######",
    ]
    return Maze(grid)


def get_large_maze(size: int = 20, seed: int = 0) -> Maze:
    grid: List[str] = []

    grid.append("#" * (size + 2))

    for r in range(size):
        row = ["#"]
        for c in range(size):
            if r == 0 and c == 0:
                row.append("S")
            elif r == size - 1 and c == size - 1:
                row.append("E")
            else:
                is_corridor_row = r % 3 == 0
                is_corridor_col = c % 3 == 0
                mix = (r * 7 + c * 13 + seed * 31) % 100

                if is_corridor_row or is_corridor_col:
                    if mix < 3 and not (r <= 1 and c <= 1) and not (r >= size - 2 and c >= size - 2):
                        row.append("#")
                    else:
                        row.append(".")
                else:
                    if mix < 20 and not (r <= 1 and c <= 1) and not (r >= size - 2 and c >= size - 2):
                        row.append("#")
                    else:
                        row.append(".")
        row.append("#")
        grid.append("".join(row))

    grid.append("#" * (size + 2))

    return Maze(grid)


def get_huge_maze(size: int = 100, seed: int = 42) -> Maze:
    """
    Generates a large maze designed to stress-test BFS implementations.
    S is at top-left, E is at bottom-right, maximizing path length.
    Uses a maze pattern with corridors to ensure a valid path exists.

    For size >= 100, basic BFS will be slow. Bidirectional BFS
    can solve these much faster by searching from both ends.
    """
    grid: List[str] = []

    grid.append("#" * (size + 2))

    for r in range(size):
        row = ["#"]
        for c in range(size):
            if r == 0 and c == 0:
                row.append("S")
            elif r == size - 1 and c == size - 1:
                row.append("E")
            else:
                # Create a maze pattern with guaranteed connectivity
                # Horizontal corridors every 4 rows, vertical passages
                is_corridor_row = (r % 4 == 0)
                is_corridor_col = (c % 4 == 0)

                # Add some randomness but keep paths open
                mix = (r * 7 + c * 13 + seed * 31) % 100

                if is_corridor_row or is_corridor_col:
                    # Keep corridors mostly open
                    if mix < 5:
                        row.append("#")
                    else:
                        row.append(".")
                else:
                    # Fill areas between corridors with walls/open based on pattern
                    if mix < 40:
                        row.append("#")
                    else:
                        row.append(".")
        row.append("#")
        grid.append("".join(row))

    grid.append("#" * (size + 2))

    return Maze(grid)


def get_spiral_maze(size: int = 50) -> Maze:
    """
    Generates a spiral maze where the path winds from outside to center.
    S at top-left corner, E near the center.
    This maze specifically benefits from bidirectional BFS because
    the path is very long but the endpoints are far apart in the search tree.
    """
    grid = [["#"] * (size + 2) for _ in range(size + 2)]

    # Carve a spiral path
    r, c = 1, 1
    dr, dc = 0, 1  # Start moving right

    path_cells = []
    visited = set()

    for _ in range(size * size):
        if (r, c) in visited:
            break
        if not (1 <= r <= size and 1 <= c <= size):
            break

        grid[r][c] = "."
        path_cells.append((r, c))
        visited.add((r, c))

        # Try to continue in current direction, or turn
        nr, nc = r + dr, c + dc
        if (nr, nc) in visited or not (1 <= nr <= size and 1 <= nc <= size):
            # Turn right: (0,1) -> (1,0) -> (0,-1) -> (-1,0) -> (0,1)
            dr, dc = dc, -dr
            nr, nc = r + dr, c + dc
            if (nr, nc) in visited or not (1 <= nr <= size and 1 <= nc <= size):
                break

        r, c = nr, nc

    # Place S at start and E near end of spiral
    if path_cells:
        sr, sc = path_cells[0]
        grid[sr][sc] = "S"

        # E at about 80% through the spiral
        end_idx = min(len(path_cells) - 1, int(len(path_cells) * 0.8))
        er, ec = path_cells[end_idx]
        grid[er][ec] = "E"

    return Maze(["".join(row) for row in grid])
