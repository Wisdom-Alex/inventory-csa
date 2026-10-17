"""API tests using FastAPI's TestClient (needs httpx)."""

import os
import tempfile
import unittest

from fastapi.testclient import TestClient

from inventory_app.api import app
from inventory_app.migrate import LEGACY_JSON, migrate


class ApiTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        os.environ["INVENTORY_DB"] = os.path.join(self.tmp.name, "api.db")
        migrate(LEGACY_JSON)
        self.client = TestClient(app)

    def tearDown(self):
        self.tmp.cleanup()
        os.environ.pop("INVENTORY_DB", None)

    def test_health(self):
        self.assertEqual(self.client.get("/health").json(), {"status": "ok"})

    def test_list_and_value(self):
        self.assertEqual(len(self.client.get("/items").json()), 4)
        self.assertEqual(self.client.get("/stock-value").json()["total_stock_value"], 3570000)

    def test_create_update_delete(self):
        r = self.client.post("/items", json={"item_name": "Cable", "quantity": 3, "price": 500})
        self.assertEqual(r.status_code, 201)
        new_id = r.json()["id"]
        self.assertEqual(self.client.patch(f"/items/{new_id}/quantity?quantity=7").json()["quantity"], 7)
        self.assertEqual(self.client.delete(f"/items/{new_id}").status_code, 204)
        self.assertEqual(self.client.get(f"/items/{new_id}").status_code, 404)

    def test_validation_error(self):
        r = self.client.post("/items", json={"item_name": "", "quantity": -1, "price": 5})
        self.assertEqual(r.status_code, 422)


if __name__ == "__main__":
    unittest.main()
