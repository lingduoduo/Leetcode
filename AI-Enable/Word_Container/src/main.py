"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from solver import Solver
from word_list import WordList
from words import get_example_words


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")

    words = get_example_words()
    wl = WordList(words)

    print(f"  Input words: {words}")
    print(f"  Valid words: {wl.get_words()}")
    print()

    solver = Solver(wl)
    containers = solver.find_containers()

    print(f"  Container words: {containers}")
    print()

    if containers:
        print("  Details:")
        for container in containers:
            # Find what it contains
            for word in wl.get_words():
                if word != container and wl.contains_as_substring(container, word):
                    print(f"    '{container}' contains '{word}'")

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
