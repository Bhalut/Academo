#!/usr/bin/env python
"""This module contains the Class Model class."""
from django.db.models import Model, CharField, TextField, FileField, ForeignKey, DateField, DateTimeField, CASCADE

from .course import Course


class CourseDetail(Model):
    """This class represents the class model."""
    name = CharField(max_length=100)
    description = TextField()
    files = FileField(upload_to="classes")
    course = ForeignKey(Course, on_delete=CASCADE)
    start_date = DateField()
    end_date = DateField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
