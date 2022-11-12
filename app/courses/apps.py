#!/usr/bin/env python
"""Courses app."""
from django.apps import AppConfig


class CoursesConfig(AppConfig):
    """Courses app config."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courses'
