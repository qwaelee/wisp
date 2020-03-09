from django.conf.urls import url

from .views import heroes_list, cloud_view, jester_view, sunflowey_view

urlpatterns = [

    url(r'^$', heroes_list.as_view(), name = 'heroes_list'),
    url(r'heroes/', heroes_list.as_view(), name = 'heroes_list'),
    url(r'hero/cloud', cloud_view.as_view(), name = 'cloud_view'),
    url(r'hero/jester', jester_view.as_view(), name = 'jester_view'),
    url(r'hero/sunflowey', sunflowey_view.as_view(), name = 'sunflowey_view'),

    ]
