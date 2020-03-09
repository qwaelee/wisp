from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class heroes_list(TemplateView)
    template_name = "home.html"
    
class cloud_view(TemplateView)
    template_name = "detail_cloud.html"
    
class jester_view(TemplateView)
    template_name = "detail_jester.html"
    
class sunflowey_view(TemplateView)
    template_name = "detail_sunflowey.html"
    

