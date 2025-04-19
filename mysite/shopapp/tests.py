from django.test import TestCase

from .utils import add_two_numbers

class AddTwoNumbers(TestCase):
    def test_add_two_numbers(self):
        result = add_two_numbers(2, 3)
        self.assertEqual(result, 5)


# class ProductCreateViewTestCase(TestCase):
#     def text_create_product(self)
