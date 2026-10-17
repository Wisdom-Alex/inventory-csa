"""Unit tests for pure business logic."""

import unittest

from inventory_app.controllers import build_summary, total_stock_value
from inventory_app.models import Item


class ControllerTests(unittest.TestCase):
    def setUp(self):
        self.items = [Item(item_name="A", quantity=2, price=100),
                      Item(item_name="B", quantity=50, price=1)]

    def test_total(self):
        self.assertEqual(total_stock_value(self.items), 250)

    def test_summary(self):
        s = build_summary(self.items)
        self.assertEqual(s["highest_stock"], "B")
        self.assertEqual(s["lowest_stock"], "A")
        self.assertEqual(s["low_stock_items"], ["A"])

    def test_empty(self):
        s = build_summary([])
        self.assertEqual(s["total_stock_value"], 0)
        self.assertIsNone(s["highest_stock"])


if __name__ == "__main__":
    unittest.main()
