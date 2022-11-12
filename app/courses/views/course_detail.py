#!/usr/bin/env python
"""This module contains the CourseView class."""
from ..models import CourseDetail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


@api_view(['GET'])
def CourseDetailsView(request):
    all_detail = CourseDetail.objects.all()

    return Response({'status': 'success', 'message': 'Course detail retrieved successfully',
                     'data': all_detail}, status=HTTP_200_OK)

@api_view(['GET'])
def CourseDetailView(request, pk):
    detail = CourseDetail.objects.get(id=pk)

    return Response({'status': 'success', 'message': 'Course detail retrieved successfully', 'data': detail},
                    status=HTTP_200_OK)
