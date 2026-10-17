"""Data access layer: all SQL lives here (SQLite, standard library)."""

from typing import Optional
import os
import sqlite3

from inventory_app.models import Item, ItemCreate

SCHEMA = """
CREATE TABLE IF NOT EXISTS items (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT    NOT NULL,
    quantity  INTEGER NOT NULL CHECK (quantity >= 0),
    price     REAL    NOT NULL CHECK (price >= 0)
);
"""


def db_path() -> str:
    """Return the database file path (env INVENTORY_DB or inventory.db)."""
    return os.environ.get("INVENTORY_DB", "inventory.db")


def connect(path: Optional[str] = None) -> sqlite3.Connection:
    """Open a connection, create the schema if needed and return it."""
    conn = sqlite3.connect(path or db_path(), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    return conn


def _to_item(row: sqlite3.Row) -> Item:
    return Item(**dict(row))


def list_items(conn: sqlite3.Connection) -> list[Item]:
    """Return every item ordered by id."""
    return [_to_item(r) for r in conn.execute("SELECT * FROM items ORDER BY id")]


def get_item(conn: sqlite3.Connection, item_id: int) -> Optional[Item]:
    """Return one item or None."""
    row = conn.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
    return _to_item(row) if row else None


def add_item(conn: sqlite3.Connection, data: ItemCreate) -> Item:
    """Insert an item and return it with its new id."""
    cur = conn.execute(
        "INSERT INTO items (item_name, quantity, price) VALUES (?, ?, ?)",
        (data.item_name, data.quantity, data.price),
    )
    conn.commit()
    return get_item(conn, cur.lastrowid)  # type: ignore[arg-type]


def update_quantity(conn: sqlite3.Connection, item_id: int, quantity: int) -> Optional[Item]:
    """Set a new quantity and return the updated item (None if missing)."""
    conn.execute("UPDATE items SET quantity = ? WHERE id = ?", (quantity, item_id))
    conn.commit()
    return get_item(conn, item_id)


def delete_item(conn: sqlite3.Connection, item_id: int) -> bool:
    """Delete an item. Returns True when a row was removed."""
    cur = conn.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    return cur.rowcount > 0


def count_items(conn: sqlite3.Connection) -> int:
    """Return the number of stored items."""
    return conn.execute("SELECT COUNT(*) FROM items").fetchone()[0]
