"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.

Key Modules

maze.py: core domain model (Position, CellType, Maze) with parsing, neighbor generation, move validation, render/path overlay.

mazes.py: maze factory/generator layer with fixed fixtures and synthetic generators:
get_simple_maze, get_small_maze, get_medium_maze
directional cases: get_directional_maze, get_directional_maze_blocked
placement case: get_anywhere_start_end_maze
scale/perf generators: get_large_maze(size, seed), get_huge_maze(size, seed), get_spiral_maze(size)

solver.py: Solver service object with solve() still unimplemented.

main.py: runnable entrypoint showing how solver is invoked and how maze/path are rendered.

test_maze.py: unit tests for maze dimensions, start/end discovery, neighbors, rendering.

test_solver.py: solver test scaffold for correctness + performance + directional behavior (most checks still commented).
"""

from mazes import get_small_maze
from solver import Solver


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")

    maze = get_small_maze()
    solver = Solver(maze)

    print("Original maze:")
    for row in maze.render():
        print(row)
    print()

    path = solver.solve()
    if path:
        print(f"Path found with {len(path)} steps:")
        print()
        for row in maze.render_with_path(path):
            print(row)
        print()
        print("Path coordinates:")
        for pos in path:
            print(f"  ({pos.row}, {pos.col})")
    else:
        print("No path found!")

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
