"""Reads inventory.py and calculates the total stock value."""

from inventory import inventory
from utils.helpers import highest_stock_item, lowest_stock_item


def total_stock_value(items):
    total = 0
    for item in items:
        # BUG (seeded for corrective maintenance): ignores quantity
        total += item["price"]
    return total


if __name__ == "__main__":
    print("Total stock value:", total_stock_value(inventory))
    print("Highest stock:", highest_stock_item(inventory)["item_name"])
    print("Lowest stock:", lowest_stock_item(inventory)["item_name"])
