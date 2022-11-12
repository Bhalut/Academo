#!/usr/bin/env python
"""This module contains the CourseView class."""
from ..models import Course, CourseDetail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


@api_view(['GET'])
def CourseView(request, pk):
    course = Course.objects.get(id=pk)
    detail = CourseDetail.objects.filter(course=course)

    return Response({'status': 'success', 'message': 'Course detail retrieved successfully',
                     'data': {'course': course, 'detail': detail}}, status=HTTP_200_OK)

@api_view(['GET'])
def CoursesView(request):
    all_courses = Course.objects.all()
    request.session.get("user")

    return Response({'status': 'success', 'message': 'Courses retrieved successfully',
                     'data': all_courses}, status=HTTP_200_OK)

