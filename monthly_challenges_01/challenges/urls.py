from django.urls import path

from . import views

urlpatterns = [
  path('january', views.january, name='january'),
  path('february', views.february, name='february'),
]
