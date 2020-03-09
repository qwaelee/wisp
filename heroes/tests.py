from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

# Create your tests here.

class HeroesListPageTest(TestCase)

    def test_heroes_home_page(self)
        response = self.client.get('/heroes')
        self.assertTemplateUsed(response, 'https://localhost:8000')

    def test_cloud_home_page(self)
       response = self.client.get('/heroes/templates')
       self.assertTemplateUsed(response, 'detail_cloud.html')

    def test_jester_home_page(self)
       response = self.client.get('/heroes/templates')
       self.assertTemplateUsed(response, 'detail_jester.html')

    def test_sunflowey_home_page(self)
       response = self.client.get('/heroes/templates')
       self.assertTemplateUsed(response, 'detail_sunflowey.html')
