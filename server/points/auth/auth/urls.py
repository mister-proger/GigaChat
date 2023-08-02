from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register),
    path('auth', views.auth),
    path('', views.index)
]
