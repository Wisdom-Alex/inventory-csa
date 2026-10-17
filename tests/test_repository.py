"""Tests for the SQLite repository and the JSON migration."""

import os
import tempfile
import unittest
from pathlib import Path

from inventory_app import repository
from inventory_app.migrate import LEGACY_JSON, migrate
from inventory_app.models import ItemCreate


class RepositoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = os.path.join(self.tmp.name, "test.db")

    def tearDown(self):
        self.tmp.cleanup()

    def test_migration_is_idempotent(self):
        self.assertEqual(migrate(LEGACY_JSON, self.db), 4)
        self.assertEqual(migrate(LEGACY_JSON, self.db), 0)

    def test_crud(self):
        conn = repository.connect(self.db)
        item = repository.add_item(conn, ItemCreate(item_name="Cable", quantity=3, price=500))
        self.assertEqual(item.id, 1)
        self.assertEqual(repository.update_quantity(conn, 1, 9).quantity, 9)
        self.assertTrue(repository.delete_item(conn, 1))
        self.assertFalse(repository.delete_item(conn, 1))
        conn.close()


if __name__ == "__main__":
    unittest.main()
