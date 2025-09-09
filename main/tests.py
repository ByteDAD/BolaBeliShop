from django.test import TestCase, Client
from .models import Product

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/burhan_always_exists/')
        self.assertEqual(response.status_code, 404)

    def test_product_creation(self):
        product = Product.objects.create(
            name="Jersey BURHAN FC",
            price=150000,
            description="Jersey original BURHAN FC",
            category="jersey",
            is_featured=True,
            stock=10,
            brand="BURHANWEAR"
        )
        self.assertEqual(product.name, "Jersey BURHAN FC")
        self.assertEqual(product.category, "jersey")
        self.assertTrue(product.is_featured)
        self.assertEqual(product.stock, 10)
        self.assertEqual(product.brand, "BURHANWEAR")

    def test_product_default_values(self):
        product = Product.objects.create(
            name="Sepatu Bola",
            price=300000,
            description="Sepatu bola untuk latihan",
            category="sepatu"
        )
        self.assertFalse(product.is_featured)
        self.assertEqual(product.stock, 0)  # default value
        self.assertIsNone(product.brand)    # default value

