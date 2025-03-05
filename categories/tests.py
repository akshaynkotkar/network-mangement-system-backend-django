from django.test import TestCase
from rest_framework.test import APIClient
from .models import Category
import json

class CategoryAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Category.objects.create(name="Test Category 1")
        Category.objects.create(name="Test Category 2")

    def test_get_categories(self):
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        print("API Response:", data)
        self.assertTrue('results' in data or isinstance(data, list)) 