"""
Provides sample nonogram puzzles for testing and benchmarking.
get_small_puzzles() returns 5x5 puzzles for debugging.
get_medium_puzzles() returns 10x10 puzzles for Phase 2 verification.
get_large_puzzles() returns 15x15 puzzles for optimization testing.
get_huge_puzzles() returns 25x25 puzzles for stress testing.
"""

import os
from typing import List

from nonogram import Nonogram


def _data_dir() -> str:
    return os.path.join(os.path.dirname(__file__), "..", "data")


def _parse_puzzle_file(filepath: str) -> List[Nonogram]:
    with open(filepath, "r") as f:
        content = f.read()

    puzzles: List[Nonogram] = []
    blocks = content.strip().split("\n\n")

    for block in blocks:
        lines = block.strip().split("\n")
        if not lines:
            continue

        dimensions = lines[0].split()
        rows = int(dimensions[0])
        cols = int(dimensions[1])

        separator_idx = -1
        for i, line in enumerate(lines):
            if line.strip() == "---":
                separator_idx = i
                break

        row_clues: List[List[int]] = []
        for i in range(1, separator_idx):
            clue = [int(x) for x in lines[i].split()]
            row_clues.append(clue)

        col_clues: List[List[int]] = []
        for i in range(separator_idx + 1, len(lines)):
            if lines[i].strip():
                clue = [int(x) for x in lines[i].split()]
                col_clues.append(clue)

        puzzles.append(Nonogram(rows, cols, row_clues, col_clues))

    return puzzles


def get_small_puzzles() -> List[Nonogram]:
    """Three 5x5 puzzles: heart, cross, arrow. Good for basic debugging."""
    return _parse_puzzle_file(os.path.join(_data_dir(), "puzzles_small.txt"))


def get_medium_puzzles() -> List[Nonogram]:
    """Three 10x10 puzzles: anchor, smiley, house. Tests basic solver correctness."""
    return _parse_puzzle_file(os.path.join(_data_dir(), "puzzles_medium.txt"))


def get_large_puzzles() -> List[Nonogram]:
    """Two 15x15 random puzzles. Requires constraint propagation to solve in time."""
    return _parse_puzzle_file(os.path.join(_data_dir(), "puzzles_large.txt"))


def get_huge_puzzles() -> List[Nonogram]:
    """One 25x25 random puzzle. Stress test for optimized solvers."""
    return _parse_puzzle_file(os.path.join(_data_dir(), "puzzles_huge.txt"))
