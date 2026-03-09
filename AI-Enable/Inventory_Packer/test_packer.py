"""Tests for Packer."""

import unittest

from item import Item, get_test_items, get_large_items
from packer import Packer
from warehouse import Warehouse


class PackerTest(unittest.TestCase):

    def test_basic_packing(self) -> None:
        warehouse = Warehouse(weight_limit=15, size_limit=15)
        packer = Packer(warehouse)
        items = get_test_items()
        assignment = packer.pack(items)
        self.assertEqual(len(assignment), len(items))
        for name, bin_id in assignment.items():
            b = warehouse.get_bins()[bin_id]
            self.assertLessEqual(b.current_weight(), b.weight_limit)
            self.assertLessEqual(b.current_size(), b.size_limit)



    def test_large_catalog(self) -> None:
        warehouse = Warehouse(weight_limit=15, size_limit=15)
        packer = Packer(warehouse)
        items = get_large_items()
        packer.pack(items)
        self.assertLess(warehouse.total_bins(), 15)


if __name__ == "__main__":
    unittest.main()
