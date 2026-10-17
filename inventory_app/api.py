"""REST API (FastAPI) exposing the inventory over HTTP."""

from collections.abc import Iterator
from sqlite3 import Connection

from fastapi import Depends, FastAPI, HTTPException, Query

from inventory_app import repository
from inventory_app.controllers import (DEFAULT_LOW_STOCK_THRESHOLD, build_summary,
                                       total_stock_value)
from inventory_app.models import Item, ItemCreate

app = FastAPI(title="Inventory API", version="2.0.0",
              description="Re-engineered inventory service (SEN 401 Lab 4).")


def get_db() -> Iterator[Connection]:
    """Provide one database connection per request and always close it."""
    conn = repository.connect()
    try:
        yield conn
    finally:
        conn.close()


@app.get("/health")
def health() -> dict:
    """Liveness probe used by Docker health checks."""
    return {"status": "ok"}


@app.get("/items", response_model=list[Item])
def read_items(conn: Connection = Depends(get_db)):
    """List all stock lines."""
    return repository.list_items(conn)


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, conn: Connection = Depends(get_db)):
    """Return one stock line or 404."""
    item = repository.get_item(conn, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", response_model=Item, status_code=201)
def create_item(data: ItemCreate, conn: Connection = Depends(get_db)):
    """Create a stock line (validated by Pydantic)."""
    return repository.add_item(conn, data)


@app.patch("/items/{item_id}/quantity", response_model=Item)
def change_quantity(item_id: int, quantity: int = Query(ge=0),
                    conn: Connection = Depends(get_db)):
    """Update the quantity of a stock line."""
    if repository.get_item(conn, item_id) is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return repository.update_quantity(conn, item_id, quantity)


@app.delete("/items/{item_id}", status_code=204)
def remove_item(item_id: int, conn: Connection = Depends(get_db)) -> None:
    """Delete a stock line."""
    if not repository.delete_item(conn, item_id):
        raise HTTPException(status_code=404, detail="Item not found")


@app.get("/stock-value")
def stock_value(conn: Connection = Depends(get_db)) -> dict:
    """Return the total stock value."""
    return {"total_stock_value": total_stock_value(repository.list_items(conn))}


@app.get("/summary")
def summary(threshold: int = DEFAULT_LOW_STOCK_THRESHOLD, conn: Connection = Depends(get_db)):
    """Return headline figures and low stock alerts."""
    return build_summary(repository.list_items(conn), threshold)
