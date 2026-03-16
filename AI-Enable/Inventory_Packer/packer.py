"""You'll implement this."""

from typing import Dict, List

from item import Item
from warehouse import Warehouse


class Packer:
    """Packs items into warehouse bins, minimizing bins used."""

    def __init__(self, warehouse: Warehouse):
        self.warehouse = warehouse

    def pack(self, items: List[Item]) -> Dict[str, int]:
        """Returns a mapping of item name -> bin_id."""
        result: Dict[str, int] = {}
        ordered_items = sorted(items, key=lambda item: (item.weight + item.size, item.weight, item.size), reverse=True)

        for item in ordered_items:
            best_bin = None
            best_score = None
            for current_bin in self.warehouse.get_bins():
                if not current_bin.can_fit(item):
                    continue

                score = (
                    current_bin.remaining_weight() - item.weight,
                    current_bin.remaining_size() - item.size,
                )
                if best_score is None or score < best_score:
                    best_bin = current_bin
                    best_score = score

            if best_bin is None:
                best_bin = self.warehouse.create_bin()

            best_bin.add_item(item)
            result[item.name] = best_bin.bin_id

        return result
