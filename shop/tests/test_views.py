from django.test import TestCase, Client

from shop.models import Product, Purchase


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.product_table = Product.objects.create(name="table", price=740, quantity_on_stock=10)

    def test_webpage_accessibility(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_purchase(self):
        self.assertEqual(Product.objects.get(id=self.product_table.id).price, 740)
        self.client.post('/purchase', data={f'quantity {self.product_table.id}': ['1'],
                                            'person': ['Ivanov'],
                                            'address': ['Svetlaya St.']})
        self.assertEqual(Product.objects.get(id=self.product_table.id).price, 740)
        self.client.post('/purchase', data={f'quantity {self.product_table.id}': ['6'],
                                            'person': ['Ivanov'],
                                            'address': ['Svetlaya St.']})
        self.assertEqual(Product.objects.get(id=self.product_table.id).quantity_on_stock, 3)
        self.assertEqual(Product.objects.get(id=self.product_table.id).price, 888)
