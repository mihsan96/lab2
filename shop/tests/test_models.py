from django.test import TestCase
from shop.models import Product, Purchase
from datetime import datetime


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="table", price=740, quantity_on_stock=10)

    def test_correctness_types(self):
        self.assertIsInstance(Product.objects.get(name="table").name, str)
        self.assertIsInstance(Product.objects.get(name="table").price, int)
        self.assertIsInstance(Product.objects.get(name="table").quantity_on_stock, int)

    def test_correctness_data(self):
        self.assertTrue(Product.objects.get(name="table").price == 740)
        self.assertTrue(Product.objects.get(name="table").quantity_on_stock == 10)


class PurchaseTestCase(TestCase):
    def setUp(self):
        self.product_table = Product.objects.create(name="table", price=740, quantity_on_stock=10)
        Purchase.objects.create(product=self.product_table,
                                person="Ivanov",
                                address="Svetlaya St.",
                                price=740,
                                quantity_purchased=1)

    def test_correctness_types(self):
        self.assertIsInstance(Purchase.objects.get(product=self.product_table).person, str)
        self.assertIsInstance(Purchase.objects.get(product=self.product_table).address, str)
        self.assertIsInstance(Purchase.objects.get(product=self.product_table).date, datetime)
        self.assertIsInstance(Purchase.objects.get(product=self.product_table).price, int)
        self.assertIsInstance(Purchase.objects.get(product=self.product_table).quantity_purchased, int)

    def test_correctness_data(self):
        self.assertTrue(Purchase.objects.get(product=self.product_table).person == "Ivanov")
        self.assertTrue(Purchase.objects.get(product=self.product_table).address == "Svetlaya St.")
        self.assertTrue(Purchase.objects.get(product=self.product_table).price == 740)
        self.assertTrue(Purchase.objects.get(product=self.product_table).quantity_purchased == 1)
