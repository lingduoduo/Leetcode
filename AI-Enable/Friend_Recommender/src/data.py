"""
Sample data for testing the social network.
"""

import os
from typing import List, Tuple

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def _load_network(filename: str) -> Tuple[List[str], List[Tuple[str, str]]]:
    filepath = os.path.join(DATA_DIR, filename)
    users: List[str] = []
    friendships: List[Tuple[str, str]] = []
    with open(filepath, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 1:
                users.append(parts[0])
            elif len(parts) == 2:
                friendships.append((parts[0], parts[1]))
    return users, friendships


def get_huge_network() -> Tuple[List[str], List[Tuple[str, str]]]:
    return _load_network("users_huge.txt")


def get_small_network() -> Tuple[List[str], List[Tuple[str, str]]]:
    users = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank",
             "Grace", "Heidi", "Ivan", "Judy", "Karl", "Liam"]
    friendships = [
        ("Alice", "Bob"),
        ("Alice", "Charlie"),
        ("Alice", "Diana"),
        ("Bob", "Charlie"),
        ("Bob", "Eve"),
        ("Charlie", "Diana"),
        ("Charlie", "Eve"),
        ("Charlie", "Frank"),
        ("Diana", "Frank"),
        ("Diana", "Grace"),
        ("Eve", "Frank"),
        ("Eve", "Heidi"),
        ("Frank", "Grace"),
        ("Frank", "Heidi"),
        ("Grace", "Ivan"),
        ("Grace", "Judy"),
        ("Heidi", "Ivan"),
        ("Ivan", "Judy"),
        ("Judy", "Karl"),
        ("Karl", "Liam"),
    ]
    return users, friendships
