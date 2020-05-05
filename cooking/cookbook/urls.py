from django.urls import path

from .views import home, hello_template

urlpatterns = [
    path('', home),
    path('template/', hello_template)
]
