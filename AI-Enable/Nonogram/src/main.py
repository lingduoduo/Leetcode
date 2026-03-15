"""Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed."""

from puzzles import get_small_puzzles
from solver import NonogramSolver


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")

    puzzles = get_small_puzzles()
    puzzle = puzzles[0]

    print("Puzzle clues:")
    print(puzzle.render_with_clues())
    print()

    solver = NonogramSolver(puzzle)
    result = solver.solve()

    if result and result.is_solved():
        print("Solved!")
        print()
        for row in result.render():
            print(row)
    else:
        print("Could not solve puzzle.")

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
