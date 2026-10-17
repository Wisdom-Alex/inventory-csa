"""Optional helper functions for the inventory."""


def highest_stock_item(items):
    return max(items, key=lambda i: i["quantity"])


def lowest_stock_item(items):
    # BUG (seeded for corrective maintenance): uses max instead of min
    return max(items, key=lambda i: i["quantity"])
