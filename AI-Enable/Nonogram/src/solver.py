"""Constraint-based Nonogram solver."""

from typing import Dict, List, Optional, Tuple

from nonogram import CellState, Nonogram


Pattern = Tuple[CellState, ...]


class NonogramSolver:
    def __init__(self, puzzle: Nonogram) -> None:
        self.puzzle = puzzle
        self._pattern_cache: Dict[Tuple[int, Tuple[int, ...]], List[Pattern]] = {}

    def solve(self) -> Optional[Nonogram]:
        row_domains = [
            self._generate_patterns(self.puzzle.cols, self.puzzle.get_row_clues(row))
            for row in range(self.puzzle.rows)
        ]
        col_domains = [
            self._generate_patterns(self.puzzle.rows, self.puzzle.get_col_clues(col))
            for col in range(self.puzzle.cols)
        ]
        return self._search(self.puzzle.clone(), row_domains, col_domains)

    def _search(
        self,
        puzzle: Nonogram,
        row_domains: List[List[Pattern]],
        col_domains: List[List[Pattern]],
    ) -> Optional[Nonogram]:
        propagated = self._propagate(puzzle, row_domains, col_domains)
        if propagated is None:
            return None

        puzzle, row_domains, col_domains = propagated
        if not puzzle.has_unknown_cells():
            return puzzle if puzzle.is_solved() else None

        branch = self._choose_branch(row_domains, col_domains)
        if branch is None:
            return None

        axis, index, candidates = branch
        for candidate in candidates:
            next_puzzle = puzzle.clone()
            next_row_domains = [list(domain) for domain in row_domains]
            next_col_domains = [list(domain) for domain in col_domains]

            if axis == "row":
                for col, state in enumerate(candidate):
                    next_puzzle.set_cell(index, col, state)
                next_row_domains[index] = [candidate]
            else:
                for row, state in enumerate(candidate):
                    next_puzzle.set_cell(row, index, state)
                next_col_domains[index] = [candidate]

            solved = self._search(next_puzzle, next_row_domains, next_col_domains)
            if solved is not None:
                return solved

        return None

    def _propagate(
        self,
        puzzle: Nonogram,
        row_domains: List[List[Pattern]],
        col_domains: List[List[Pattern]],
    ) -> Optional[Tuple[Nonogram, List[List[Pattern]], List[List[Pattern]]]]:
        changed = True
        while changed:
            changed = False

            for row in range(puzzle.rows):
                line = tuple(puzzle.get_row(row))
                filtered = [pattern for pattern in row_domains[row] if self._matches(line, pattern)]
                if not filtered:
                    return None
                if len(filtered) != len(row_domains[row]):
                    row_domains[row] = filtered
                    changed = True
                for col, state in self._forced_cells(filtered).items():
                    current = puzzle.get_cell(row, col)
                    if current == CellState.UNKNOWN:
                        puzzle.set_cell(row, col, state)
                        changed = True
                    elif current != state:
                        return None

            for col in range(puzzle.cols):
                line = tuple(puzzle.get_col(col))
                filtered = [pattern for pattern in col_domains[col] if self._matches(line, pattern)]
                if not filtered:
                    return None
                if len(filtered) != len(col_domains[col]):
                    col_domains[col] = filtered
                    changed = True
                for row, state in self._forced_cells(filtered).items():
                    current = puzzle.get_cell(row, col)
                    if current == CellState.UNKNOWN:
                        puzzle.set_cell(row, col, state)
                        changed = True
                    elif current != state:
                        return None

        return puzzle, row_domains, col_domains

    def _choose_branch(
        self,
        row_domains: List[List[Pattern]],
        col_domains: List[List[Pattern]],
    ) -> Optional[Tuple[str, int, List[Pattern]]]:
        best_axis: Optional[str] = None
        best_index = -1
        best_candidates: List[Pattern] = []

        for row, domain in enumerate(row_domains):
            if 1 < len(domain) and (not best_candidates or len(domain) < len(best_candidates)):
                best_axis = "row"
                best_index = row
                best_candidates = domain

        for col, domain in enumerate(col_domains):
            if 1 < len(domain) and (not best_candidates or len(domain) < len(best_candidates)):
                best_axis = "col"
                best_index = col
                best_candidates = domain

        if best_axis is None:
            return None
        return best_axis, best_index, best_candidates

    def _forced_cells(self, patterns: List[Pattern]) -> Dict[int, CellState]:
        forced: Dict[int, CellState] = {}
        if not patterns:
            return forced

        for index in range(len(patterns[0])):
            value = patterns[0][index]
            if all(pattern[index] == value for pattern in patterns[1:]):
                forced[index] = value
        return forced

    def _matches(self, line: Pattern, pattern: Pattern) -> bool:
        return all(cell == CellState.UNKNOWN or cell == state for cell, state in zip(line, pattern))

    def _generate_patterns(self, length: int, clues: List[int]) -> List[Pattern]:
        key = (length, tuple(clues))
        if key in self._pattern_cache:
            return self._pattern_cache[key]

        if not clues or clues == [0]:
            patterns = [tuple([CellState.EMPTY] * length)]
            self._pattern_cache[key] = patterns
            return patterns

        patterns: List[Pattern] = []
        working = [CellState.EMPTY] * length

        def place(run_index: int, start: int) -> None:
            if run_index == len(clues):
                patterns.append(tuple(working))
                return

            run_length = clues[run_index]
            remaining = clues[run_index + 1 :]
            min_remaining = sum(remaining) + len(remaining) if remaining else 0
            max_start = length - run_length - min_remaining

            for pos in range(start, max_start + 1):
                for offset in range(run_length):
                    working[pos + offset] = CellState.FILLED

                place(run_index + 1, pos + run_length + 1)

                for offset in range(run_length):
                    working[pos + offset] = CellState.EMPTY

        place(0, 0)
        self._pattern_cache[key] = patterns
        return patterns
