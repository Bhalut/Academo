#!/usr/bin/env python
"""This module contains the LogoutView class."""
from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


@api_view(['GET'])
def LogoutView(request):
    logout(request)

    return Response({'status': 'success', 'message': 'User logged out successfully'}, status=HTTP_200_OK)
