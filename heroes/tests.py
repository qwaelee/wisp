from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

# Create your tests here.

class Home_Test(TestCase):

    def test_heroes_home_page(self):
        response = self.client.get('/heroes/')
        self.assertTemplateUsed(response, 'home.html')

class Cloud_Test(TestCase):

    def test_cloud_home_page(self):
       response = self.client.get('/hero/cloud/')
       self.assertTemplateUsed(response, 'detail_cloud.html')

class Jester_Test(TestCase):
    
    def test_jester_home_page(self):
       response = self.client.get('/hero/jester/')
       self.assertTemplateUsed(response, 'detail_jester.html')

class Sunflowey_Test(TestCase):

    def test_sunflowey_home_page(self):
       response = self.client.get('/hero/sunflowey/')
       self.assertTemplateUsed(response, 'detail_sunflowey.html')
