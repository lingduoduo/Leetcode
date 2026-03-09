"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from checker import Checker
from dictionary import get_test_dictionary


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")

    dictionary = get_test_dictionary()
    checker = Checker(dictionary)

    misspelled = ["teh", "helo", "thier", "hourse", "knwo"]
    for word in misspelled:
        suggestions = checker.suggest(word, max_suggestions=3)
        if suggestions:
            print(f"  '{word}' -> {suggestions}")
        else:
            print(f"  '{word}' -> no suggestions")

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
