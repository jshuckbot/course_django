from django.urls import path

from aboutmeapp import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("about/", views.about_me, name="about"),
]
