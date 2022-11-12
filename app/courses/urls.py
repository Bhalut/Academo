#!/usr/bin/env python
"""URLs for the courses' app."""
from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path

from .views import CoursesView, CourseView, CourseDetailView, CourseDetailsView

router = DefaultRouter(trailing_slash=False)

# router.register(r'courses/', CoursesView, 'courses')
# router.register(r'^courses/(?P<pk>[0-9]+)/$', CourseView, 'course-detail')
# router.register(r'^courses/(?P<pk>[0-9]+)/details/$', CourseDetailsView, 'course-details')
# router.register(r'^courses/(?P<pk>[0-9]+)/details/(?P<pk>[0-9]+)$', CourseDetailView, 'course-details')
#
# urlpatterns = router.urls

urlpatterns = [
    re_path(r'^courses/', CoursesView, name='courses'),
    re_path(r'^courses/(?P<pk>[0-9]+)/$', CourseView, name='course'),
    re_path(r'^courses/(?P<pk>[0-9]+)/details/$', CourseDetailsView, name='course-details'),
    re_path(r'^courses/(?P<pk>[0-9]+)/details/(?P<pk_detail>[0-9]+)$', CourseDetailView, name='course-detail'),
]
