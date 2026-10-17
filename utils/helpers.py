"""Optional helper functions for the inventory."""


def highest_stock_item(items):
    """Return the item with the largest quantity, or None if empty."""
    return max(items, key=lambda i: i["quantity"], default=None)


def lowest_stock_item(items):
    """Return the item with the smallest quantity, or None if empty."""
    return min(items, key=lambda i: i["quantity"], default=None)
