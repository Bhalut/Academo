#!/usr/bin/env python
"""URLs for the users' app."""
from django.urls import path

from .views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('register/', RegisterView, name='register'),
    path('login/', LoginView, name='logout'),
    path('logout/', LogoutView, name='logout'),
]
