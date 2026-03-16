"""
Provides item definitions and sample catalogs.
get_test_items() is useful when developing your Packer.
"""

from typing import List, NamedTuple

from dataclasses import dataclass


@dataclass
class Item(NamedTuple):
    name: str
    weight: int
    size: int


def get_test_items() -> List[Item]:
    return [
        Item("Monitor", 8, 6),
        Item("Keyboard", 2, 3),
        Item("Mouse", 1, 1),
        Item("Laptop", 5, 4),
        Item("Printer", 10, 8),
        Item("Webcam", 1, 1),
        Item("Speaker", 3, 3),
        Item("Tablet", 2, 3),
    ]


def get_large_items() -> List[Item]:
    items = []
    for i in range(30):
        w = (i % 7) + 1
        s = (i % 5) + 1
        items.append(Item(f"item-{i:03d}", w, s))
    return items
