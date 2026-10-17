"""Optional helper functions for the inventory."""

from typing import Optional
from inventory import Item


def highest_stock_item(items: list[Item]) -> Optional[Item]:
    """Return the item with the largest quantity, or None if empty."""
    return max(items, key=lambda i: i.quantity, default=None)


def lowest_stock_item(items: list[Item]) -> Optional[Item]:
    """Return the item with the smallest quantity, or None if empty."""
    return min(items, key=lambda i: i.quantity, default=None)


def low_stock_items(items: list[Item], threshold: int = 10) -> list[Item]:
    """Return items whose quantity is at or below ``threshold``."""
    return [i for i in items if i.quantity <= threshold]
