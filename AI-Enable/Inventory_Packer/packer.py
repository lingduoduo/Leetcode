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
        result = {}
        
        for item in items:
            # Try to find an existing bin that can fit this item
            placed = False
            for bin in self.warehouse.get_bins():
                if bin.can_fit(item):
                    bin.add_item(item)
                    result[item.name] = bin.bin_id
                    placed = True
                    break
            
            # If no existing bin can fit the item, create a new bin
            if not placed:
                new_bin = self.warehouse.create_bin()
                new_bin.add_item(item)
                result[item.name] = new_bin.bin_id
        
        return result
