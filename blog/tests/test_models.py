from django.test import TestCase
from ..models import Blog

class CatTestCase(TestCase):
    def setUp(self):
        Blog.objects.create(title="tama")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        title = Blog.objects.get(title="tama")
        self.assertEqual(title.title,"tama")
