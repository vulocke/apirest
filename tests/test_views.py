# tests/test_views.py
from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.

    def test_product_found(self):
        response = self.client.get("/api/v1/products/1")
        print(response.status_code)
        product = response.json
        self.assertIsInstance(product, dict)
        self.assertEqual(product.get('id'), 1)

    def test_product_not_found(self):
        response = self.client.get("/api/v1/products/4")
        print(response.status_code)
        product = response.json
        self.assertEqual(product, None)

    def test_product_delete(self):
        response = self.client.get("/api/v1/products/1")
        print("code retour delete: " + str(response.status_code))
