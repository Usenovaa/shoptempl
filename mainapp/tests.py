from django.test import TestCase
from .models import Product, Category
from django.contrib.auth import get_user_model
User = get_user_model()

class ProductTest(TestCase):
    def setUp(self) -> None:
        category = Category.objects.create(
            name='ca'
        )
        user = User.objects.create(
            username='aaa',
            email='ggg',
            password='12we'
        )
        product = Product.objects.create(
            quantity='8',
            title='yiujd',
            price=1223,
            category=category,
            owner=user

        )

    def test_values(self):
        product = Product.objects.get(title='yiujd')
        self.assertIsInstance(product.quantity, int)
        self.assertIsInstance(product.category, Category)
        # self.assertIsInstance(product.category, User)

