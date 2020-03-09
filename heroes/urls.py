from django.conf.urls import url

from .views import heroes_list, cloud_view, jester_view, sunflowey_view

urlPatterns = [

    url("heroes/templates", heroes_list.as_view(), name = "heroes_list"),
    url("heroes/templates", cloud_view.as_view(), name = "cloud_view"),
    url("heroes/templates", jester_view.as_view(), name = "jester_view"),
    url("heroes/templates", sunflowey_view.as_view(), name = "sunflowey_view")

    ]
