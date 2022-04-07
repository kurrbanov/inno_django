from django.test import TestCase

from requests import get

from application.form import CategoryForm


class TestCategoryForm(TestCase):
    def test_name_less_5(self):
        category_data = {"name": "abc"}
        category = CategoryForm(data=category_data)
        self.assertEqual(False, category.is_valid())

    def test_name_greater_25(self):
        category_data = {"name": "abc" * 10}
        category = CategoryForm(data=category_data)
        self.assertEqual(False, category.is_valid())


class TestSecret(TestCase):
    def test_top_secret(self):
        response = get("http://127.0.0.1:8000/top_secret")
        self.assertEqual(response.status_code, 403)
