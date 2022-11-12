#!/usr/bin/env python
"""This module contains the RegisterView class."""
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


@api_view(['POST'])
def LoginView(request):
    if request.user.is_authenticated:
        return Response({'status': 'error', 'message': 'Is Already authenticated'}, status=HTTP_400_BAD_REQUEST)

    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)

        return Response({'status': 'success', 'message': f'User {username} logged in successfully'}, status=HTTP_200_OK)

    return Response({'status': 'error', 'message': 'Invalid credentials'}, status=HTTP_400_BAD_REQUEST)
