from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("/list", views.ProfileListView.as_view(), name="list")
]
