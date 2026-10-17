"""Domain models shared by the CLI, repository and REST API."""

from typing import Optional
from pydantic import BaseModel, Field, computed_field


class ItemCreate(BaseModel):
    """Payload used to create a stock line."""

    item_name: str = Field(min_length=1, max_length=100)
    quantity: int = Field(ge=0)
    price: float = Field(ge=0)


class Item(ItemCreate):
    """A stored stock line with an optional database id."""

    id: Optional[int] = None

    @computed_field  # included automatically in API responses
    @property
    def value(self) -> float:
        """Stock value of this line (quantity * price)."""
        return self.quantity * self.price
