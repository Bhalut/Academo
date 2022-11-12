#!/usr/bin/env python
"""This module contains the Course Model class."""
from django.db.models import Model, CharField, TextField, ImageField, DateField, DateTimeField


class Course(Model):
    """This class represents the course model."""
    name = CharField(max_length=100)
    description = TextField()
    # thumb = ImageField(upload_to='thumb/', default='thumb/default.png')
    start_date = DateField()
    end_date = DateField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
