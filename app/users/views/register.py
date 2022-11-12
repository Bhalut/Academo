#!/usr/bin/env python
"""This module contains the RegisterView class."""
from django.contrib.auth.models import Group
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from ..serializers import UserSerializer


@api_view(['POST'])
def RegisterView(request):
    if request.user.is_authenticated:
        return Response({'status': 'error', 'message': 'Is Already authenticated'}, status=HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        username = serializer.data.get('username')

        group = Group.objects.get(name='student')
        serializer.instance.groups.add(group)

        return Response({'status': 'success', 'message': f'User created successfully {username}'},
                        status=HTTP_201_CREATED)

    return Response({'status': 'error', 'message': serializer.errors}, status=HTTP_400_BAD_REQUEST)
