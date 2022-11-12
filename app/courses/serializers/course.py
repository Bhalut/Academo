#!/usr/bin/env python
"""This module contains the CourseSerializer class."""
from rest_framework import serializers

from ..models import Course


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for Course model.
    """
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')