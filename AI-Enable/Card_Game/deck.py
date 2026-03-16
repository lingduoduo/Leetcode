"""
Provides card definitions and deck utilities.
get_test_deck() is useful when developing your Solver.
"""

import random
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


class Suit(Enum):
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
    SPADES = "♠"


@dataclass(frozen=True, slots=True)
class Card:
    value: int
    suit: Suit

    def __str__(self) -> str:
        return f"{self.value}{self.suit.value}"


def create_deck() -> List[Card]:
    return [Card(value, suit) for value in range(1, 10) for suit in Suit]


def shuffle_deck(cards: List[Card], seed: Optional[int] = None) -> List[Card]:
    rng = random.Random(seed)
    shuffled = list(cards)
    rng.shuffle(shuffled)
    return shuffled


def get_test_deck() -> List[Card]:
    return shuffle_deck(create_deck(), seed=42)


def get_standard_deck() -> List[Card]:
    return shuffle_deck(create_deck())
