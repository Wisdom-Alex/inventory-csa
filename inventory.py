"""Inventory data using a validated, immutable dataclass (Python 3.9+)."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    """One stock line: item_name, quantity and unit price in NGN."""

    item_name: str
    quantity: int
    price: float

    def __post_init__(self) -> None:
        if not self.item_name.strip():
            raise ValueError("item_name must not be blank")
        if self.quantity < 0 or self.price < 0:
            raise ValueError("quantity and price must not be negative")

    @property
    def value(self) -> float:
        """Stock value of this line (quantity * price)."""
        return self.quantity * self.price


inventory: list[Item] = [
    Item("Laptop", 5, 450_000),
    Item("Mouse", 40, 6_500),
    Item("Keyboard", 25, 12_000),
    Item("Monitor", 8, 95_000),
]
