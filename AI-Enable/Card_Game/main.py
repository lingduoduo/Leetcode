"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from card_game import CardGame
from solver import Solver


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")

    game = CardGame(seed=42)
    print(f"Starting grid ({game.grid_rows}x{game.grid_cols}):")
    print(game.display_grid())
    print(f"Deck: {game.cards_remaining_in_deck()} cards remaining")
    print()

    solver = Solver(game)
    turns = solver.play_game()

    print(f"Game over after {turns} turns")
    for i, picked in enumerate(game.history):
        cards_str = ", ".join(str(c) for c in picked)
        values_str = " + ".join(str(c.value) for c in picked)
        print(f"  Turn {i + 1}: [{cards_str}] ({values_str} = {sum(c.value for c in picked)})")

    print()
    stats = Solver.simulate_games(
        num_games=100,
        strategy="play_game",
        grid_rows=4,
        grid_cols=6,
    )
    print("Greedy strategy over 100 seeded 4x6 games:")
    print(f"  Perfect games: {stats.perfect_games}/{stats.games_played}")
    print(f"  Perfect rate: {stats.perfect_rate:.0%}")
    print(f"  Average score: {stats.average_score:.1f}/{game.perfect_score}")

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
