from django.test import TestCase
from django.test import Client
from ..models import Blog

class CatTestCase(TestCase):
    def setUp(self):
        c=Client()
        Blog.objects.create(title="tama")

    def test_animals_can_speak(self):
        """testing CatViewSet"""
        c=Client()
        pk=Blog.objects.get(title="tama").pk
        response1 = c.get('/blog/')
        response2 = c.get('/blog/detail/'+str(pk))

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
