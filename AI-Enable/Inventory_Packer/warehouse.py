"""Read this first."""

from typing import List

from item import Item


class Bin:
    def __init__(self, bin_id: int, weight_limit: int, size_limit: int):
        self.bin_id = bin_id
        self.weight_limit = weight_limit
        self.size_limit = size_limit
        self._items: List[Item] = []

    def current_weight(self) -> int:
        return sum(item.weight for item in self._items)

    def current_size(self) -> int:
        return sum(item.size for item in self._items)

    def can_fit(self, item: Item) -> bool:
        return (
            (self.current_weight() + item.weight) <= self.weight_limit
            and (self.current_size() + item.size) <= self.size_limit
        )

    def add_item(self, item: Item) -> None:
        if not self.can_fit(item):
            raise ValueError(
                f"'{item.name}' does not fit in bin {self.bin_id}"
            )
        self._items.append(item)

    def get_items(self) -> List[Item]:
        return list(self._items)

    def remaining_weight(self) -> int:
        return self.weight_limit - self.current_weight()

    def remaining_size(self) -> int:
        return self.size_limit - self.current_size()


class Warehouse:
    def __init__(self, weight_limit: int = 15, size_limit: int = 10):
        self._weight_limit = weight_limit
        self._size_limit = size_limit
        self._bins: List[Bin] = []

    def create_bin(self) -> Bin:
        new_bin = Bin(len(self._bins), self._weight_limit, self._size_limit)
        self._bins.append(new_bin)
        return new_bin

    def get_bins(self) -> List[Bin]:
        return list(self._bins)

    def total_bins(self) -> int:
        return len(self._bins)

    def total_items(self) -> int:
        return sum(len(b.get_items()) for b in self._bins)
