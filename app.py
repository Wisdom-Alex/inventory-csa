"""Reads inventory.py and calculates the total stock value."""

from inventory import Item, inventory
from utils.helpers import highest_stock_item, lowest_stock_item


def total_stock_value(items: list[Item]) -> float:
    """Return the sum of quantity * price for every item."""
    return sum(item.value for item in items)


if __name__ == "__main__":
    print("Total stock value:", total_stock_value(inventory))
    print("Highest stock:", highest_stock_item(inventory).item_name)
    print("Lowest stock:", lowest_stock_item(inventory).item_name)
