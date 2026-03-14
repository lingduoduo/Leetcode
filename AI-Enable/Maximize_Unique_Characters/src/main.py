"""Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed."""

from solver import MaxUniqueSolver
from word_list import WordList
from words import get_months


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")

    words, alphabet = get_months()
    wl = WordList(words, alphabet)

    print(f"  Alphabet: {alphabet}")
    print(f"  Words: {words}")
    print(f"  Valid words: {wl.valid_words()}")

    solver = MaxUniqueSolver(wl)
    result = solver.solve()

    print(f"  Selected: {result}")
    print(f"  Unique chars: {wl.total_unique_chars(result)}")

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
